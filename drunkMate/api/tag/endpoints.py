from fastapi import APIRouter, Depends

from drunkMate.api.tag import contract
from drunkMate.core.cruds import tag_crud, user_crud
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/tag_api/create_cocktail_tag")
async def create_cocktail_tag(tag_creation: contract.TagBase,
                              current_user: User = Depends(user_crud.get_current_user)):
    await tag_crud.create_tag(tag_creation.dict())


@router.get("/tag_api/get_cocktail_tags")
async def get_cocktail_tags():
    return await tag_crud.get_tags()


@router.post("/tag_api/create_ingredient_tag")
async def create_ingredient_tag(tag_creation: contract.TagBase,
                                current_user: User = Depends(user_crud.get_current_user)):
    await tag_crud.create_tag(tag_creation.dict(), is_ingredient=True)


@router.get("/tag_api/get_ingredient_tags")
async def get_ingredient_tags():
    return await tag_crud.get_tags(is_ingredient=True)
