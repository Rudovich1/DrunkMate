from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from drunkMate.api.comment import contract
from drunkMate.core.cruds import comment_crud, user_crud
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/comment_api/post_comment")
async def post_comment(comment_creation: contract.CommentRequest,
                       current_user: User = Depends(user_crud.get_current_user)):
    comment_creation = dict(comment_creation)


@router.delete("/coment api/delete comment")
async def delete_comment(comment: contract.CommentRequest,
                         current_user: User = Depends(user_crud.get_current_user)):

    if current_user.role == 1 or str(current_user.dict()['_id']) == comment.author.id:
        await comment_crud.delete_comment(str(comment.dict()['_id']), comment.cocktail_id)

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not enough rights",
        headers={"WWW-Authenticate": "Bearer"},
    )
