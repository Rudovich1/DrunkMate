from sqlmodel import SQLModel, Field, BLOB
from typing import List
from bson.objectid import ObjectId

from typing import Optional


class Ingredient(SQLModel):
    ingredient_id: ObjectId
    amount: int
    unit: int


class CocktailBase(SQLModel):
    author: ObjectId
    name: str = Field(min_length=1, max_length=170, unique=True)
    description: str = Field(max_length=500, nullable=True)
    rating: Optional[float]
    tags: List[ObjectId]
    #image: Optional[BLOB] = None
    recipe: str = Field(max_length=5000)
    strength: int
    ingredients: List[Ingredient]
    comments: List[ObjectId]
    parent_cocktail: Optional[ObjectId]


class Cocktail(CocktailBase):
    id: str = Field(primary_key=True)


class CocktailCreate(CocktailBase):
    pass
