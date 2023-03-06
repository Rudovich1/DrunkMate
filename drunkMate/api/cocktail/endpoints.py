from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile, File
from starlette import status

from drunkMate.core.cruds import cocktail_crud, user_crud
from drunkMate.api.cocktail import contract
from drunkMate.api.user.contract import User
from drunkMate.api.image.endpoints import post_image

router = APIRouter()


@router.post("/cocktail_api/post_cocktail")
async def post_cocktail(
    cocktail: contract.CPostCocktail,
    current_user: User = Depends(user_crud.get_current_user),
):
    guid = await cocktail_crud.post_cocktail(cocktail.dict(), current_user["_id"])
    return guid


@router.put("/cocktail_api/put_cocktail")
async def put_cocktail(
    cocktail: contract.CPutCocktail,
    current_user: User = Depends(user_crud.get_current_user),
):
    if current_user["role"] == 1 or str(current_user["_id"]) == str(
        (await cocktail_crud.get_cocktail(cocktail.id))["author"]
    ):
        await cocktail_crud.put_cocktail(cocktail.dict())
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get("/cocktail_api/get_cocktail/{id}")
async def get_cocktail(id: str):
    cocktail = await cocktail_crud.get_cocktail(id)
    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The cocktail does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return cocktail


@router.post("/cocktail_api/get_cocktails")
async def get_cocktails(
    cocktail_info: contract.CGetCocktails = contract.CGetCocktails(),
):
    return await cocktail_crud.get_cocktails(
        cocktail_info.search, cocktail_info.tags, cocktail_info.ingredients
    )


@router.delete("/cocktail_api/delete_cocktail")
async def delete_cocktail(
    cocktail: contract.CDeleteCocktail,
    current_user: User = Depends(user_crud.get_current_user),
):
    if current_user["role"] == 1 or current_user["login"] == cocktail.login:
        await cocktail_crud.delete_cocktail(cocktail.id)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )
