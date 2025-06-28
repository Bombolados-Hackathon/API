from fastapi import APIRouter
from app.api.v1.endpoints import users, tasks

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(tasks.router)
