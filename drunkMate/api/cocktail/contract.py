from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from typing import List


class Ingredient(BaseModel):
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


class CPostCocktail(BaseModel):
    name: str = Field(min_length=1, max_length=170)
    description: str = Field(max_length=500)
    tags: List[str]
    #image: Optional[BLOB] = None
    recipe: str = Field(max_length=5000)
    strength: int
    ingredients: List[Ingredient]
    parent_cocktails: List[ParentCocktail]
    

class CPutCocktail(CPostCocktail):
    id: str
    login: str


class CGetCocktail(BaseModel):
    id: str


class CDeleteCocktail(BaseModel):
    id: str
    login: str

