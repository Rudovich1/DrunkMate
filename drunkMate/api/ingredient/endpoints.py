from fastapi import APIRouter, Depends, HTTPException, status

from drunkMate.api.ingredient import contract
from drunkMate.core.cruds import ingredient_crud, user_crud
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/ingredient_api/post_ingredient")
async def post_ingredient(post_ingredient: contract.CPostIngredient,
                            current_user: User = Depends(user_crud.get_current_user)):
    await ingredient_crud.post_ingredient(post_ingredient.dict())


@router.get("/ingredient_api/get_ingredients")
async def get_ingredients():
    return await ingredient_crud.get_ingredients()


# @router.put("/ingredient_api/put_ingredient")
# async def put_ingredient(put_ingredient: contract.CPutIngredient,
#                          current_user: User = Depends(user_crud.get_current_user)):
    
#     if current_user['role'] == 1:
#         await ingredient_crud.put_ingredient(put_ingredient.dict())
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not enough rights",
#             headers={"WWW-Authenticate": "Bearer"},
#         )


@router.delete("/ingredient_api/delete_ingredient")
async def delete_ingredient(delete_ingredient: contract.CDeleteIngredient,
                              current_user: User = Depends(user_crud.get_current_user)):
    if current_user['role'] == 1:
        await ingredient_crud.delete_ingredient(delete_ingredient.name)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )
