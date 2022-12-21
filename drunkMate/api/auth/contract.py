from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str# = Field(alias="access_token")
    token_type: str# = Field(alias="token_type")


class UserBase(BaseModel):
    login: str = Field(min_length=1, max_length=50)
    name: str = Field(min_length=1, max_length=50)
    #image


class UserRegistration(UserBase):
    password: str


class UserLogin(BaseModel):
    login: str
    password: str
