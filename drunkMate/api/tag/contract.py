from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class Tag(TagBase):
    id: str
