from drunkMate.core import repository
from bson.objectid import ObjectId
from fastapi import HTTPException, status


async def get_cocktail(cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)
    if cocktail is None:
        return None
    return {
        "id": str(cocktail["_id"]),
        "name": cocktail["name"],
        "description": cocktail["description"],
        "rating": cocktail["rating"],
        "tags": cocktail["tags"],
        "recipe": cocktail["recipe"],
        "author": str(cocktail["author"]),
        "strength": cocktail["strength"],
        "ingredients": list(cocktail["ingredients"]),
        "comments": list(map(lambda x: str(x), cocktail["comments"])),
        "parent_cocktails": cocktail["parent_cocktails"],
    }


async def post_cocktail(item: dict, author_id: str):
    cocktail = {
        "name": item["name"],
        "description": item["description"],
        "rating": None,
        "tags": item["tags"],
        "recipe": item["recipe"],
        "author": ObjectId(author_id),
        "strength": item["strength"],
        "ingredients": item["ingredients"],
        "comments": [],
        "parent_cocktails": item["parent_cocktails"],
    }

    for ingredient in item["ingredients"]:
        if repository.get_ingredient(ingredient["name"]) is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There are no declared ingredients",
                headers={"WWW-Authenticate": "Bearer"},
            )

    cock_id = str(repository.post_cocktail(cocktail))

    for tag in item["tags"]:
        repository.post_tag({"name": tag})

    return cock_id


async def get_cocktails(search="", tags=[], ingredients=[]):
    cocktails = list(repository.get_cocktails(search, tags, ingredients))
    res_cocktails = []
    for cocktail in cocktails:
        res_cocktails.append(
            {
                "id": str(cocktail["_id"]),
                "name": cocktail["name"],
                "rating": cocktail["rating"],
                "tags": cocktail["tags"],
                "author": str(cocktail["author"]),
                "strength": cocktail["strength"],
            }
        )

    return res_cocktails


async def put_cocktail(item: dict):
    if repository.get_cocktail(item["id"]) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The cocktail does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )

    for ingredient in item["ingredients"]:
        if repository.get_ingredient(ingredient["name"]) is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"The ingredient does not exist",
                headers={"WWW-Authenticate": "Bearer"},
            )

    for tag in item["tags"]:
        if repository.get_tag(False, tag) is None:
            repository.post_tag({"name": tag}, is_ingredient=False)

    repository.put_cocktail(
        item["id"],
        {
            "name": item["name"],
            "description": item["description"],
            "tags": item["tags"],
            "recipe": item["recipe"],
            "strength": item["strength"],
            "ingredients": item["ingredients"],
            "parent_cocktails": item["parent_cocktails"],
        },
    )


async def delete_cocktail(cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)

    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The cocktail does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )

    for comment in cocktail["comments"]:
        repository.delete_comment(str(comment))

    repository.delete_cocktail(cocktail_id)
