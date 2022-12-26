from bson import ObjectId
from fastapi import HTTPException
from starlette import status

from drunkMate.core import repository
from drunkMate.core.cruds import cocktail_crud


async def post_comment(cocktail_id: str, author_id: str, text: str, rating: int):
    cocktail = await cocktail_crud.get_cocktail(cocktail_id)

    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The cocktail does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )

    comments = cocktail['comments']

    for comment in comments:
        comment = repository.get_comment(str(comment))
        author = comment['author']
        if str(author) == author_id:
            new_rating = (cocktail['rating']*len(cocktail['comments'])-comment['rating']+rating)/len(cocktail['comments'])
            repository.put_cocktail(cocktail_id, {'rating': new_rating})
            repository.update_comment(str(comment['_id']), text, rating)
            return

    comment_id = repository.post_comment(author_id, text, rating)

    if cocktail['rating'] is None:
        new_rating = rating
    else:
        new_rating = (cocktail['rating'] * len(cocktail['comments']) + rating)/(len(cocktail['comments']) + 1)
    cocktail['comments'].append(ObjectId(comment_id))
    repository.put_cocktail(cocktail_id, {'rating': new_rating, 'comments': cocktail['comments']})


async def delete_comment(comment_id: str, cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)
    comment = repository.get_comment(comment_id)
    
    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The cocktail does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The comment does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if len(cocktail['comments']) == 1:
        cocktail['rating'] = None
    else:
        cocktail['rating'] = (cocktail['rating'] * len(cocktail['comments']) - comment['rating']) / (len(cocktail['comments']) - 1)

    cocktail['comments'] = cocktail['comments'].remove(ObjectId(comment_id))

    repository.delete_comment(comment_id)


async def get_comments(cocktail_id: str):
    repository.get_comments(cocktail_id)
