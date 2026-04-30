from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api.routes import health_router, user_router
from app.models.base import Base
from app.core.db import engine

from dotenv import load_dotenv
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(health_router)
app.include_router(user_router)