from sqlmodel import SQLModel, Field
from bson.objectid import ObjectId
from typing import List


class Ingredient(SQLModel):
    name: str = Field(min_length=1, max_length=170)
    #image:
    tags: List[ObjectId]
    description: str = Field(max_length=500, nullable=True)
