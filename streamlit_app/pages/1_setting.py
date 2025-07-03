import streamlit as st

st.set_page_config(page_title="Settings", layout="wide")
st.title("⚙️ Settings")

st.markdown("### API Keys & Preferences")
st.text_input("OpenAI API Key", placeholder="sk-...", type="password")
st.text_input("Google Calendar Service Account Path", placeholder="credentials/service_account.json")
st.selectbox("Preferred Timezone", ["Asia/Kolkata", "UTC", "America/New_York", "Europe/London"])
st.button("Save Settings")