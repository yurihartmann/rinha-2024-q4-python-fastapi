from fastapi import FastAPI

from app.routes import app_routes

app = FastAPI()

app.include_router(app_routes)

