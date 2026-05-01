from app.api.routes import health_router, user_router
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()
app.include_router(health_router)
app.include_router(user_router)
