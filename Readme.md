Here’s a clean and professional `README.md` for your **Calendar-agent** project, ready to be published on GitHub:

---

```markdown
# 📅 Conversational AI Calendar Booking Agent

A smart AI-powered assistant that helps you **book appointments** on your Google Calendar using **natural language conversation**.

Built with:
- 🧠 OpenAI GPT
- 🚀 FastAPI (backend)
- 🎨 Streamlit (frontend UI)
- �� LangChain (agent flow)
- 📆 Google Calendar API

---

## ✨ Features

✅ Natural language appointment booking  
✅ Google Calendar integration (via OAuth or Service Account)  
✅ Clean chat-based UI with calendar visualization  
✅ Dark/Light theme toggle  
✅ Event confirmation with tick mark on calendar

---

## 🖥️ Live Demo (Optional)

Coming soon...

---

## 📁 Folder Structure

```
Calender-agent/
├── backend/                         # Backend app (FastAPI)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI entrypoint
│   │   ├── config.py                # Environment loading
│   │   ├── routes/                  # API routes
│   │   │   ├── __init__.py
│   │   │   └── calendar.py
│   │   ├── services/                # Event logic & LLM integration
│   │   │   ├── __init__.py
│   │   │   └── event_service.py
│   │   └── utils/                   # Google Calendar integration
│   │       ├── __init__.py
│   │       └── google_calendar.py
│   ├── Dockerfile                   # (Optional) Backend-specific Dockerfile
│   └── requirements.txt             # Backend dependencies
│
├── streamlit_app/                  # Frontend (Streamlit)
│   ├── app.py                      # Main UI app
│   ├── pages/                      # Multi-page support (Settings, History)
│   │   ├── 1_Settings.py
│   │   └── 2_History.py
│   ├── components/                 # Custom UI components (optional)
│   └── style.css                   # Custom CSS for Streamlit theme
│
├── credentials/                    # Google service credentials (add to .gitignore)
│   └── client_secret.json
│
├── .env                            # Environment variables (never commit)
├── .env.example                    # Sample environment variables
├── .gitignore                      # Ignored files and folders
├── Dockerfile                      # Combined Dockerfile (frontend + backend)
├── requirements.txt                # Combined requirements (for Docker use)
├── README.md                       # Project documentation
└── LICENSE                         # Optional MIT or other license

---

## 🧪 Installation

### 1. Clone the Repo

bash
git clone https://github.com/your-username/Calendar-agent.git
cd Calendar-agent

### 2. Create `.env` file

> Create a `.env` file (never commit it) in project root:

env
OPENAI_API_KEY=your-openai-api-key
GOOGLE_CREDENTIALS_PATH=credentials/client_secret.json
TIMEZONE=Asia/Kolkata
CALENDAR_ID=your-google-calendar-id
```

### 3. Install Dependencies

Using `venv`:

bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

---

## 🚀 Run the App

### 1. Start the backend:

bash
cd backend
uvicorn app.main:app --reload

### 2. Start the frontend (in new terminal):

bash
cd streamlit_app
streamlit run app.py


Then open: [http://localhost:8501](http://localhost:8501)


## 🐳 Docker Setup (Optional)

## ✅ Example Prompts

text
• Book a dentist appointment on Friday at 2 PM
• Call Alice tomorrow at 5 PM for 30 minutes
• Meeting with team on July 8 at 11 AM


## 🔐 Secrets & Security

Make sure to:

* Never commit `.env` or `credentials/`
* Use `.env.example` for sharing variables

## �� Roadmap

* [x] Calendar view with appointment marker
* [x] Dark/Light mode toggle
* [ ] Appointment history page
* [ ] Recurring event support
* [ ] Database integration

---

## 🤝 Contributing

Pull requests welcome. For major changes, open an issue first.


## 📄 License

[MIT](LICENSE)


## ✨ Credits

Made with ❤️ by [Ramkrishna Dixit](mailto:rkdrkd2121@gmail.com)
