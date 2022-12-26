from pydantic import BaseModel, Field
from typing import List

from drunkMate.api.tag import contract
from drunkMate.api.tag.contract import TagBase


class IngredientBase(BaseModel):
    name: str
    #image:
    description: str = Field(max_length=500)


class Ingredient(IngredientBase):
    id: str


class CGetIngredients(IngredientBase):
    tags: List[str]


class IngredientRequest(IngredientBase):
    tags: List[str]


class CPostIngredient(BaseModel):
    name: str
    description: str = Field(max_length=500)
    tags: list[str]
    
    
class CPutIngredient(CPostIngredient):
    old_name: str
    

class CDeleteIngredient(BaseModel):
    name: str
    
    
class CGetIngredientsByTags(BaseModel):
    tags: list[str]