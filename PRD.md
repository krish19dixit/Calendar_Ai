

# Conversational AI Calendar Booking Agent — MVP

**Version:** 1.0
**Owner:** \[Your Name]
**Date:** 2025-07-01

---

##  Product Overview

Build a conversational AI agent that assists **individuals** and **service providers** in booking appointments directly into **Google Calendar**, through a natural, back-and-forth **chat interface**.

The system leverages **OpenAI GPT** for conversation, **FastAPI** for backend processing, **LangGraph/LangChain** for agent orchestration, and **Streamlit** for the frontend UI.

---

##  Goals

* Allow users to chat naturally to schedule meetings or services
* Provide calendar availability
* Book appointments into each provider’s individual Google Calendar
* Confirm appointments via chat and email

---

##  Target Users

* **Individuals**: Booking meetings with themselves or others
* **Service Providers**: Therapists, coaches, consultants who offer 1:1 appointments

---

## Features & Functional Requirements

### 1. Provider Selection

* Dropdown menu in the UI to select a service provider
* Loads provider-specific `config.json` file

### 2. Chat-Based Booking

* Users chat with the AI assistant via Streamlit interface
* Natural conversation (e.g., “Can I book a 1-hour consultation tomorrow afternoon?”)

### 3. Appointment Types

* Default: "Meeting" (30 mins)
* Support for custom appointment types with set durations
* Defined in `config.json`, e.g.:

  ```json
  {
    "appointment_types": {
      "Meeting": 30,
      "Consultation": 60,
      "Deep Dive": 90
    }
  }
  ```

### 4. Calendar Integration

* Each provider has their **own Google Calendar**
* Booking is done using a **Google Service Account**
* Calendar must be **pre-shared** with the Service Account
* Calendar availability = time slots not blocked by existing events

### 5. Booking Flow

* Parse user intent (appointment type, date, time)
* Show available time slots
* Confirm time and book event
* Add summary to chat
* If email provided, send confirmation email

### 6. Confirmation

* Booking confirmation shown in chat
* If email is provided by the user:

  * Send confirmation email (via SMTP or a mail service API)

---

##  Technical Architecture

### Frontend:

* **Streamlit** app
* Dropdown to select provider
* Chat window to interact with agent

### Backend:

* **FastAPI** server
* Handles request routing, calendar logic, booking logic

### Agent:

* **LangGraph** (preferred) or **LangChain** for conversation flow
* Integrates with OpenAI GPT for intent recognition and dialogue handling

### Calendar:

* **Google Calendar API**
* Uses **Service Account JSON** for auth
* Each provider’s calendar shared with service account
* Events created based on appointment type and selected time

---

##  File Structure

```
📁 app/
 ┣ 📄 main.py              # FastAPI entry point
 ┣ 📄 agent.py             # LangGraph logic
 ┣ 📄 calendar.py          # Google Calendar API integration
 ┣ 📄 email.py             # Email confirmation sender
 ┣ 📁 configs/             # One config.json per provider
 ┃ ┗ 📄 jane_doe.json
 ┣ 📄 ui.py                # Streamlit UI with chat + dropdown
 ┗ 📄 requirements.txt
```

---

##  Non-Functional Requirements

* Fast and responsive (<2s roundtrip on booking flow)
* Streamlit UI mobile-friendly
* Scalable for up to 10 providers in MVP
* Secure handling of service account credentials

---

##  Security Notes

* Service Account JSON must be stored securely (env or vault)
* No OAuth required, but provider calendars must be shared manually
* User emails are optional and only used for confirmations

---

##  Future Considerations (Post-MVP)

* OAuth login for providers
* Admin UI to edit `config.json`
* Automatic buffer/working hour logic
* Time zone support
* Calendar invite attendee support

---
