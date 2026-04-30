from fastapi import FastAPI
from .api.routes.health import router
from .models.base import Base
from .core.db import engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI()
app.include_router(router)

app.on_event("startup")
async def startup_event():
  Base.metadata.create_all(bind=engine)