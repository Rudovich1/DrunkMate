from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from drunkMate.api.comment import contract
from drunkMate.core.cruds import comment_crud, user_crud
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/comment_api/post_comment")
async def post_comment(data: contract.CPostComment,
                       current_user: User = Depends(user_crud.get_current_user)):

    await comment_crud.post_comment(data.cocktail_id, str(current_user['_id']), data.text, data.rating)


@router.post("/comment_api/get_comments")
async def get_comments(cocktail_id: str):
    await comment_crud.get_comments(cocktail_id)


@router.delete("/comment_api/delete_comment")
async def delete_comment(comment: contract.CDeleteComment,
                         current_user: User = Depends(user_crud.get_current_user)):

    if current_user['role'] == 1 or current_user.dict()['login'] == comment.author_login:
        await comment_crud.delete_comment(str(comment.dict()['_id']), comment.cocktail_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough rights",
            headers={"WWW-Authenticate": "Bearer"},
        )
