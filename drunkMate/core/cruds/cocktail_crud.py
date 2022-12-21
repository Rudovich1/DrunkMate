from drunkMate.core import repository


async def get_cocktail(cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)

    return cocktail
