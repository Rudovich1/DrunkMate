from fastapi import APIRouter

from drunkMate.api.comment import contract
from drunkMate.core.cruds import comment_crud

router = APIRouter()


@router.post("/comment_api/post_comment")
async def post_comment(comment_creation: contract.CommentRequest):
    comment_crud
