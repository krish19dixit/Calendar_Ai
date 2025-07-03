import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.config import settings
from pydantic import SecretStr

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    api_key=SecretStr(settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY else None
)

prompt = ChatPromptTemplate.from_template("""
You are a calendar assistant. Extract event details from this message.

Respond only with a JSON object like:
{{
  "summary": "...",
  "description": "...",
  "start_time": "YYYY-MM-DDTHH:MM:SS",
  "end_time": "YYYY-MM-DDTHH:MM:SS"
}}

Defaults:
- Duration = 60 mins if not mentioned.
- Use today's date if missing.
- Timezone = {timezone}

Message: {message}
""")

def extract_event_info(message: str):
    chain = prompt | llm
    try:
        response = chain.invoke({"message": message, "timezone": settings.TIMEZONE})
        content = response.content
        if isinstance(content, str):
            return json.loads(content)
        elif isinstance(content, list) and content and isinstance(content[0], str):
            return json.loads(content[0])
        return None
    except Exception:
        return None