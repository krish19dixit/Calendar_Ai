from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.calendar import router as calendar_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calendar_router)