from fastapi import APIRouter, Depends

from drunkMate.api.comment import contract
from drunkMate.core.cruds import comment_crud, user_crud
from drunkMate.api.user.contract import User

router = APIRouter()


@router.post("/comment_api/post_comment")
async def post_comment(comment_creation: contract.CommentRequest,
                       current_user: contract.UserWithId = Depends(user_crud.get_current_user)):
    comment_creation = dict(comment_creation)
    current_user.
    comment_crud
