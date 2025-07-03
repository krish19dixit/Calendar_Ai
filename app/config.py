import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")
    TIMEZONE = os.getenv("TIMEZONE")
    CALENDAR_ID=os.getenv("CALENDAR_ID")

settings = Settings()
