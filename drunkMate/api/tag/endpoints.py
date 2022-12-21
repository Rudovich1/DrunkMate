from fastapi import APIRouter

from drunkMate.api.tag import contract
from drunkMate.core.cruds import tag_crud

router = APIRouter()


@router.post("/tag_api/create_cocktail_tag")
async def create_cocktail_tag(tag_creation: contract.TagBase):
    await tag_crud.create_tag(tag_creation.dict())


@router.get("/tag_api/get_cocktail_tags")
async def get_cocktail_tags():
    return await tag_crud.get_tags()


@router.post("/tag_api/create_ingredient_tag")
async def create_ingredient_tag(tag_creation: contract.TagBase):
    await tag_crud.create_tag(tag_creation.dict(), is_ingredient=True)


@router.get("/tag_api/get_ingredient_tags")
async def get_ingredient_tags():
    return await tag_crud.get_tags(is_ingredient=True)
