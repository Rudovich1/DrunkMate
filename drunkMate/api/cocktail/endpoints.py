from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from drunkMate.core.cruds import cocktail_crud, user_crud
from drunkMate.api.cocktail import contract
from drunkMate.api.user.contract import User

router = APIRouter()


@router.get("/cocktail_api/get_cocktail/{id}", response_model=contract.CGetCocktail)
async def get_cocktail(id: str):
    cocktail = await cocktail_crud.get_cocktail(id)
    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such resource",
            headers={"WWW-Authenticate": "Bearer"},
        )
    respond = contract.CGetCocktail(
        id=str(cocktail["_id"]),
        author=str(cocktail["author"]),
        name=cocktail["name"],
        description=cocktail["description"],
        rating=cocktail["rating"],
        tags=list(map(lambda x: str(x), cocktail["tags"])),
        # image: Optional[BLOB] = None
        recipe=cocktail["recipe"],
        strength=cocktail["strength"],
        ingredients=cocktail["ingredients"],
        comments=list(map(lambda x: str(x), cocktail["comments"])),
        parent_cocktail=cocktail["parent_cocktail"]
    )


@router.post("/cocktail_api/get_cocktail/{id}")
async def create_cocktail(cocktail_create: contract.CPostIngredient,
                          current_user: User = Depends(user_crud.get_current_user)):
    pass
