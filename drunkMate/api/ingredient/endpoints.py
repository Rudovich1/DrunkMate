from fastapi import APIRouter, Depends, HTTPException, status

from drunkMate.api.ingredient import contract
from drunkMate.core.cruds import ingredient_crud, user_crud
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/ingredient_api/post_ingredient")
async def post_ingredient(post_ingredient: contract.CPostIngredient,
                            current_user: User = Depends(user_crud.get_current_user)):
    await ingredient_crud.post_ingredient(post_ingredient.dict())


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

@router.put("/ingredient_api/put_ingredient")
async def put_ingredient(put_ingredient: contract.CPutIngredient,
                         current_user: User = Depends(user_crud.get_current_user)):
    
    if current_user['role'] == 1:
        await ingredient_crud.put_ingredient(put_ingredient.dict(), current_user['_id'])
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )
        