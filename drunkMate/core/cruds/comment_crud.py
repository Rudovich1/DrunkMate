from drunkMate.core import repository
from drunkMate.core.cruds import cocktail_crud


async def post_comment():
    repository


async def delete_comment(comment_id: str, cocktail_id: str):
    await cocktail_crud.delete_comment(comment_id, cocktail_id)
    repository.delete_comment(comment_id)

