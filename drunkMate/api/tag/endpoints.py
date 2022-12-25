from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from drunkMate.api.tag import contract
from drunkMate.core.cruds import tag_crud, user_crud
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/tag_api/create_cocktail_tag")
async def post_cocktail_tag(tag: contract.CPostCocktailTag,
                              current_user: User = Depends(user_crud.get_current_user)):
    print(current_user.role)
    ans = await tag_crud.create_tag(tag.dict())


@router.get("/tag_api/get_cocktail_tags")
async def get_cocktail_tags():
    return await tag_crud.get_tags()


@router.delete("/tag_api/delete_cocktail_tag")
async def delete_cocktail_tag(tag: contract.CDeleteCocktailTag,
                              current_user: User = Depends(user_crud.get_current_user)):
    if current_user['role'] == 1:
        await tag_crud.delete_tag(tag.name, current_user['_id'])
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.post("/tag_api/create_ingredient_tag")
async def post_ingredient_tag(tag: contract.CPostIngredientTag,
                                current_user: User = Depends(user_crud.get_current_user)):
    await tag_crud.create_tag(tag.dict(), is_ingredient=True)


@router.get("/tag_api/get_ingredient_tags")
async def get_ingredient_tags():
    return await tag_crud.get_tags(is_ingredient=True)


@router.delete("/tag_api/delete_ingredient_tag")
async def delete_ingredient_tag(tag: contract.CDeleteIngredientTag,
                              current_user: User = Depends(user_crud.get_current_user)):
    if current_user['role'] == 1:
        await tag_crud.delete_tag(tag.name, current_user['_id'], is_ingredient=True)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )