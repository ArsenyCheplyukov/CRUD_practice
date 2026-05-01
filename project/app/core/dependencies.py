# core/dependencies.py

from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from fastapi import Depends


def get_user_repository():
    return UserRepository()


def get_user_service(
    repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repo)
