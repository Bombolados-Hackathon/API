from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import API_V1_STR

app = FastAPI(title="API Hackathon – AVA", version="1.0.0")
app.include_router(api_router, prefix=API_V1_STR)
