from typing import Annotated

from pydantic import BaseModel, StringConstraints

Username = Annotated[
    str,
    StringConstraints(
        min_length=3,
        max_length=50,
        strip_whitespace=True,
        pattern=r"^[a-zA-Z0-9_]+$",
    ),
]


class UserCreate(BaseModel):
    name: Username


class UserRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
