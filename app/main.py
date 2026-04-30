from fastapi import FastAPI
from api.routes.health import router
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI()
app.include_router(router)