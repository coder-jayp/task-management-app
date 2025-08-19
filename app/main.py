from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(title="Task Management APP")

app.include_router(tasks.router)