from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
from app.config import settings
import json

SCOPES = ["https://www.googleapis.com/auth/calendar"]

credentials = service_account.Credentials.from_service_account_file(
    settings.GOOGLE_CREDENTIALS_PATH, scopes=SCOPES
)

service = build("calendar", "v3", credentials=credentials)

def create_event_on_google_calendar(event_data):
    event = {
        "summary": event_data.get("summary", "Untitled Event"),
        "description": event_data.get("description", ""),
        "start": {
            "dateTime": event_data.get("start_time"),
            "timeZone": settings.TIMEZONE,
        },
        "end": {
            "dateTime": event_data.get("end_time"),
            "timeZone": settings.TIMEZONE,
        },
    }
    created_event = service.events().insert(calendarId=settings.CALENDAR_ID, body=event).execute()
    return created_event