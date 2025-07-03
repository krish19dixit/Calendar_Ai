from fastapi import APIRouter, Request
from app.agents.langchain_agent import extract_event_info
from app.utils.google_calendar import create_event_on_google_calendar

router = APIRouter()

@router.post("/chat")
def chat(payload: dict):
    message = payload.get("message", "")
    event_data = extract_event_info(message)
    if event_data:
        event = create_event_on_google_calendar(event_data)
        return {
            "response": f"Event booked: <a href='{event['htmlLink']}' target='_blank'>View on Calendar</a>",
            "event_data": event_data  # 🆕 returning parsed details
        }
    return {"response": "Sorry, I couldn’t understand that."}
