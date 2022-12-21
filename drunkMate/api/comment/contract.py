from pydantic import BaseModel, Field


class Author(BaseModel):
    id: str
    name: str


class CommentBase(BaseModel):
    text: str = Field(max_length=1000)
    rating: int


class CommentRequest(CommentBase):
    cocktail_id: str


class CommentResponse(CommentBase):
    author: Author
