from drunkMate.core import repository
from bson.objectid import ObjectId


async def get_cocktail(cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)

    return cocktail


async def delete_comment(comment_id: str, cocktail_id: str):

    cocktail = await get_cocktail(cocktail_id)
    comment = repository.get_comment(cocktail_id)

    cocktail['rating'] = (cocktail['rating']*len(cocktail['comments']) - comment['rating'])/(len(cocktail['comments']) - 1)

    cocktail['comments'] = cocktail['comments'].remove(ObjectId(comment_id))