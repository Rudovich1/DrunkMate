from sqlmodel import SQLModel, Field, BLOB

from typing import Optional


class UserBase(SQLModel):
    login: str = Field(min_length=1, max_length=50)
    name: str = Field(min_length=1, max_length=50)
    hashed_password: str
    #image: Optional[BLOB] = None
    role: int


class User(UserBase, table=True, extend_existing=True):
    id: str = Field(primary_key=True)


class UserCreate(UserBase):
    pass