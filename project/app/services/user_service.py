from app.models import User
from app.repositories import UserRepository
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create_user(self, session: AsyncSession, name: str) -> User:
        # get user by name
        user = await self.repo.get_by_name(session, name)
        # if user exists raise error
        if user:
            raise ValueError(f"User with name {name} already exists")
        # if user does not exist create it and return
        user = await self.repo.create(session, name)
        # if race condition appeared (two users created at the same time)
        try:
            await session.commit()
        except IntegrityError:
            raise ValueError(f"User with name {name} already exists")
        await session.refresh(user)
        return user

    async def get_user(self, session: AsyncSession, user_id: int) -> User | None:
        return await self.repo.get_by_id(session, user_id)

    async def get_user_by_name(self, session: AsyncSession, name: str) -> User | None:
        return await self.repo.get_by_name(session, name)

    async def list_users(self, session: AsyncSession) -> list[User]:
        return await self.repo.get_all(session)
