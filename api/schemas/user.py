from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: Optional[str]
    full_name: Optional[str]
    email: Optional[str]


class UserIn(UserBase):
    email: str
    username: str
    password: str


class UserUpdate(UserBase):
    password: Optional[str]
