from app.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UserRepository:
    async def create(self, session: AsyncSession, name: str) -> User:

        user = User(name=name)
        session.add(user)
        return user

    async def get_by_id(self, session: AsyncSession, user_id: int) -> User | None:
        user = await session.execute(select(User).where(User.id == user_id))
        return user.scalar_one_or_none()

    async def get_by_name(self, session: AsyncSession, name: str) -> User | None:
        user = await session.execute(select(User).where(User.name == name))
        return user.scalar_one_or_none()

    async def get_all(self, session: AsyncSession) -> list[User]:
        all_users = await session.execute(select(User))
        return all_users.scalars().all()
