from sqlmodel import SQLModel, Field
from bson.objectid import ObjectId


class Comment(SQLModel):
    text: str = Field(max_length=1000)
    rating: int
    author: ObjectId
