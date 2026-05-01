from .base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User
    from .comments import Comment


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship(back_populates="post")

    def __repr__(self):
        return f"Post(id={self.id!r}, title={self.title!r}, content={self.content!r})"
