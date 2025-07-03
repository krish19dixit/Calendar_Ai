import streamlit as st

st.set_page_config(page_title="History", layout="wide")
st.title("📜 Booking History")

st.info("In a future version, this page will show events pulled from Google Calendar API.")

demo_events = [
    {"title": "Kickoff Call", "date": "2025-07-05", "time": "10:00 AM"},
    {"title": "Dentist", "date": "2025-07-06", "time": "2:00 PM"},
    {"title": "Consultation", "date": "2025-07-07", "time": "5:00 PM"},
]

for event in demo_events:
    st.markdown(f"- **{event['title']}** on `{event['date']}` at `{event['time']}`")
