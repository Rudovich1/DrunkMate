from fastapi import APIRouter, HTTPException
from starlette import status

from drunkMate.core.cruds import cocktail_crud
from drunkMate.api.cocktail import contract

router = APIRouter()


@router.get("/cocktail_api/get_cocktail/{id}", response_model=contract.Cocktail)
async def get_cocktail(id: str):
    cocktail = await cocktail_crud.get_cocktail(id)
    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such resource",
            headers={"WWW-Authenticate": "Bearer"},
        )
    respond = contract.Cocktail(
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
