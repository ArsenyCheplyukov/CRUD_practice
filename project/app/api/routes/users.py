from app.core.db import get_db
from app.core.dependencies import get_user_service
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get(
    "/",
    response_model=list[UserRead],
    status_code=status.HTTP_200_OK,
)
async def list_users(
    session: AsyncSession = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    """List all users"""
    return await service.list_users(session)


@user_router.get(
    "/{user_id}",
    response_model=UserRead,
    status_code=status.HTTP_200_OK,
)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    """Get user by id"""
    user = await service.get_user(session, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_db),
    service: UserService = Depends(get_user_service),
):
    try:
        user = await service.create_user(session, user_in.name)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return user
