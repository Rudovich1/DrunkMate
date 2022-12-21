from pydantic import BaseModel, Field
from bson.objectid import ObjectId

from drunkMate.api.user import contract


class CPostComment(BaseModel):
    text: str
    rating: int
    cocktail_id: str
    author_id: str


class Author(BaseModel):
    id: str
    name: str


class CommentBase(BaseModel):
    text: str = Field(max_length=1000)
    rating: int


class CommentRequest(BaseModel):
    cocktail_id: str


class CommentDeletionRequest(CommentRequest):
    author: Author


class User(contract.User):
    _id: ObjectId
    role: int
