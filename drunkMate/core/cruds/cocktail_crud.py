from drunkMate.core import repository
from bson.objectid import ObjectId


async def get_cocktail(cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)

    return cocktail


async def add_comment(comment_id, cocktail_id):
    pass
