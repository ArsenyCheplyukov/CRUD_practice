from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.core.dependencies import get_user_service
from app.services.user_service import UserService
from fastapi import status

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/", status_code=status.HTTP_200_OK)
async def list_users(session: AsyncSession = Depends(get_db),
                     service: UserService = Depends(get_user_service)) -> dict:
  """Get all users"""
  users = await service.list_users(session)
  return {"users": users}


@user_router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int,
                   session: AsyncSession = Depends(get_db),
                   service: UserService = Depends(get_user_service)) -> dict:
  """Get user by id"""
  user = await service.get_user(session, user_id)
  if user is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
  return {"user": user}


@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(name: str,
                      session: AsyncSession = Depends(get_db),
                      service: UserService = Depends(get_user_service)) -> dict:
  try:
    user = await service.create_user(session, name)
  except ValueError as e:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
  return {"user": user}