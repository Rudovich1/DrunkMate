from pydantic import BaseModel, Field
from typing import List

from drunkMate.api.tag import contract


class IngredientBase(BaseModel):
    name: str
    #image:
    description: str = Field(max_length=500)


class Ingredient(IngredientBase):
    id: str


class IngredientResponse(Ingredient):
    tags: List[contract.Tag]


class IngredientRequest(IngredientBase):
    tags: List[str]


class CPostIngredient(BaseModel):
    name: str
    description: str = Field(max_length=500)
    
    
class CPutIngredient(BaseModel):
    name: str
    new_name: str
    description: str = Field(max_length=500)
    