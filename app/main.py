import uvicorn
from fastapi import FastAPI

from app.database.database import Database
from app.routes import app_routes

app = FastAPI()
db = Database(
    db_url="postgresql+asyncpg://localhost:5433/postgres"
)

app.include_router(app_routes)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
