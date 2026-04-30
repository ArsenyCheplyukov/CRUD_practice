# core/dependencies.py

from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from fastapi import Depends

def get_user_repository():
  return UserRepository()

def get_user_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
  return UserService(repo)