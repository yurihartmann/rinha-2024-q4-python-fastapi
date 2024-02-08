import uvicorn
from fastapi import FastAPI

from app.routes import app_routes

app = FastAPI()

app.include_router(app_routes)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
