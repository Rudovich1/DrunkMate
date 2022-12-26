from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from drunkMate.core.cruds import cocktail_crud, user_crud
from drunkMate.api.cocktail import contract
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/cocktail_api/post_cocktail")
async def post_cocktail(cocktail: contract.CPostCocktail,
                        current_user: User = Depends(user_crud.get_current_user)):
    
    await cocktail_crud.post_cocktail(cocktail.dict(), current_user['_id'])


@router.put("/cocktail_api/put_cocktail")
async def put_cocktail(cocktail: contract.CPutCocktail,
                       current_user: User = Depends(user_crud.get_current_user)):

    if current_user['role'] == 1 or current_user['login'] == cocktail.login:
        await cocktail_crud.put_cocktail(cocktail.id, cocktail.dict())
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get("/cocktail_api/get_cocktail/{id}")
async def get_cocktail(id: str):
    return await cocktail_crud.get_cocktail(id)
    
    
@router.get('/cocktail_api/get_cocktails')
async def get_cocktails():
    return await cocktail_crud.get_cocktails()
    
    
@router.delete('/cocktail_api/delete_cocktail')
async def delete_cocktail(cocktail: contract.CDeleteCocktail,
                          current_user: User = Depends(user_crud.get_current_user)):
    
    if current_user['role'] == 1 or current_user['login'] == cocktail.login:
        await cocktail_crud.delete_cocktail(cocktail.id)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.get('/cocktail_api/get_cocktails_by_tags')
async def get_cocktail_by_tags(tags: list[str]):
    return await cocktail_crud.get_cocktails_by_tags(tags)


@router.get('/cocktail_api/get_cocktails_by_ingredients')
async def get_cocktail_by_ingredients(ingredients: list[str]):
    return await cocktail_crud.get_cocktails_by_ingredients(ingredients)
