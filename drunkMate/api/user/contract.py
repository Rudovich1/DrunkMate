from bson.objectid import ObjectId

from pydantic import BaseModel, Field


class User(BaseModel):
    login: str = Field(min_length=1, max_length=50)
    name: str = Field(min_length=1, max_length=50)
    role: int = 0
    #image