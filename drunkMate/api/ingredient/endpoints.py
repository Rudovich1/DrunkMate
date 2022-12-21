from fastapi import APIRouter, Depends

from drunkMate.api.ingredient import contract
from drunkMate.core.cruds import ingredient_crud, user_crud
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/ingredient_api/post_ingredient")
async def create_ingredient(ingredient_creation: contract.IngredientBase,
                            current_user: User = Depends(user_crud.get_current_user)):
    await ingredient_crud.create_ingredient(ingredient_creation.dict())


@router.get("/ingredient_api/get_ingredients", response_model=list[contract.IngredientResponse])
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
