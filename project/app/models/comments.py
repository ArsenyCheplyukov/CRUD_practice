import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .posts import Post
    from .users import User


class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    date_created: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    user: Mapped["User"] = relationship(back_populates="comments")
    post: Mapped["Post"] = relationship(back_populates="comments")

    def __repr__(self):
        return f"Comment(id={self.id!r}, content={self.content!r}, date_created={self.date_created!r}, user_id={self.user_id!r}, post_id={self.post_id!r})"
