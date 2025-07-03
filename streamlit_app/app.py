import streamlit as st
import requests
from streamlit_calendar import calendar
import datetime

st.set_page_config(page_title="AI Calendar Assistant", page_icon="📅", layout="wide")

mode = st.radio("Select Theme:", ["🌞 Light Mode", "🌙 Dark Mode"], horizontal=True)

if mode == "🌙 Dark Mode":
    st.markdown("""
        <style>
            body { background: linear-gradient(to bottom right, #1e1e1e, #2c2c2c); color: white; }
            .navbar, .hero, .footer { background-color: #2a2a2a !important; color: white !important; }
            .stButton > button, .stTextInput > div > div > input { font-size: 1.2rem; color: white; background-color: #333333; border: 1px solid #666; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body { background: linear-gradient(to bottom right, #f9fafb, #e0f2fe); color: black; }
            .navbar { background-color: #ffffffdd; padding: 1rem; border-bottom: 1px solid #ccc; }
            .hero { padding: 2rem; background: linear-gradient(to right, #dbeafe, #eff6ff); border-radius: 12px; margin-top: 1rem; }
            .footer { margin-top: 4rem; padding: 1rem; text-align: center; font-size: 0.9rem; color: gray; }
            .stButton > button, .stTextInput > div > div > input { font-size: 1.2rem; color: black; background-color: white; border: 1px solid #ccc; }
        </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='navbar'><h3>📅 AI Calendar Assistant</h3></div>", unsafe_allow_html=True)
st.markdown("<div class='hero'><h1>Schedule smarter with AI 🤖</h1><p>Use natural language to book events directly to your Google Calendar.</p></div>", unsafe_allow_html=True)

st.subheader("📝 Book Your Appointment")
st.markdown("Enter your request (e.g., 'Book a meeting with John on Thursday at 3 PM')")
user_input = st.text_input("Your message:", placeholder="e.g., Dentist appointment on Friday at 2 PM")
submit = st.button("Book Appointment")

confirmed_event = None
calendar_events = []

if submit and user_input:
    with st.spinner("Talking to assistant..."):
        try:
            res = requests.post("http://localhost:8000/chat", json={"message": user_input})
            reply = res.json().get("response", "Sorry, something went wrong.")
            confirmed_event = res.json().get("event_data", None)

            st.success("✅ Appointment booked!")
            st.markdown(reply, unsafe_allow_html=True)

            st.markdown("### 📌 Confirmed Event Details")
            if confirmed_event:
                st.json(confirmed_event)
                calendar_events.append({
                    "title": f"✅ Appointment: {confirmed_event['summary']}",
                    "start": confirmed_event["start_time"],
                    "end": confirmed_event["end_time"],
                    "color": "#22c55e"
                })
            else:
                st.info(f"\"{user_input}\" was added to your calendar.")
        except Exception as e:
            st.error(f"❌ Failed to connect: {e}")

st.subheader("📆 Upcoming Calendar Events")
calendar_height = 400
calendar(events=calendar_events, options={
    "initialView": "dayGridMonth",
    "height": calendar_height,
    "eventDisplay": "block",
    "eventTextColor": "white"
})

st.markdown("<div class='footer'>Built with ❤️ using Streamlit, FastAPI, Langchain, and OpenAI.<br>&copy; 2025 Calendar Assistant</div>", unsafe_allow_html=True)
