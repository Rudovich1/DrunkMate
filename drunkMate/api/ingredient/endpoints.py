from fastapi import APIRouter

from drunkMate.api.ingredient import contract
from drunkMate.core.cruds import ingredient_crud

router = APIRouter()


@router.post("/ingredient_api/post_cocktail")
async def create_ingredient(ingredient_creation: contract.IngredientBase):
    await ingredient_crud.create_ingredient(ingredient_creation.dict())


@router.get("/ingredient_api/post_cocktail")
async def get_ingredients():
    ingredients = list(await ingredient_crud.get_ingredients())
    resp = []
    for item in ingredients:
        resp.append(
            contract.Ingredient(
                id=str(item['_id']),
                name=item['name'],
                tags=item['tags'],
                description=item['description']
            )
        )
    return resp
