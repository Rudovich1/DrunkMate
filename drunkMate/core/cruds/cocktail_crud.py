from drunkMate.core import repository
from bson.objectid import ObjectId


async def get_cocktail(cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)

    return cocktail


async def create_cocktail(name: str,
                          description: str,
                          recipe: str,
                          author_id: str,
                          strength: int):
    cocktail = {
        'name': name,
        'description': description,
        'rating': None,
        'tags': [],
        'recipe': recipe,
        'author': ObjectId(author_id),
        'strength': strength
    }
