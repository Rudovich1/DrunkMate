from pydantic import BaseModel, Field
from bson.objectid import ObjectId

from drunkMate.api.user import contract


class Author(BaseModel):
    id: str
    name: str


class CommentBase(BaseModel):
    text: str = Field(max_length=1000)
    rating: int


class CommentRequest(CommentBase):
    cocktail_id: str


class CommentDeletionRequest(CommentRequest):
    author: Author


class User(contract.User):
    _id: ObjectId
    role: int
