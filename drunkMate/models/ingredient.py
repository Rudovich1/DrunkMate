from sqlmodel import SQLModel, Field
from bson.objectid import ObjectId
from typing import List

from drunkMate.models import tag


class TagWithId(tag.Tag):
    id: ObjectId


class Ingredient(SQLModel):
    name: str = Field(min_length=1, max_length=170)
    #image:
    tags: List[TagWithId]
    description: str = Field(max_length=500, nullable=True)
