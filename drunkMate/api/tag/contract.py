from pydantic import BaseModel, Field


class TagBase(BaseModel):
    name: str = Field(min_length=1, max_length=50)


class Tag(TagBase):
    id: str
    
    
class CPostCocktailTag(TagBase): pass


class CDeleteCocktailTag(TagBase): pass


class CPostIngredientTag(TagBase): pass


class CDeleteIngredientTag(TagBase): pass


class CGetIngredientTags(BaseModel):
    search : str = ""
    

class CGetCocktailTags(CGetIngredientTags): pass