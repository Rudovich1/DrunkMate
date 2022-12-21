from drunkMate.core import repository
from drunkMate.core.cruds import cocktail_crud


async def post_comment(cocktail_id: str, author_id: str, text: str, rating: int):
    cocktail = await cocktail_crud.get_cocktail(cocktail_id)

    repository.create_comment()


async def delete_comment(comment_id: str, cocktail_id: str):
    await cocktail_crud.delete_comment(comment_id, cocktail_id)
    repository.delete_comment(comment_id)

