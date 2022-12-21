from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from typing import List


class Ingredient(BaseModel):
    id: str
    name: str
    amount: int
    unit: int


class Tag(BaseModel):
    id: str
    name: str


class Comment(BaseModel):
    id: str
    author_id: str
    author_name: str
    text: str
    rate: int


class ParentCocktail(BaseModel):
    id: str
    name: str


class CocktailBase(BaseModel):
    author: str
    name: str = Field(min_length=1, max_length=170, unique=True)
    description: str = Field(max_length=500, nullable=True)
    rating: float | None = None
    tags: List[Tag]
    #image: Optional[BLOB] = None
    recipe: str = Field(max_length=5000)
    strength: int
    ingredients: List[Ingredient]
    comments: List[Comment]
    parent_cocktail: ParentCocktail | None = None


class Cocktail(CocktailBase):
    id: str