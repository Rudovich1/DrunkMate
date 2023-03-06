from fastapi import APIRouter, Depends

from drunkMate.core.cruds import user_crud
from drunkMate.api.user import contract

router = APIRouter()


@router.get("/user_api/get_user", response_model=contract.User)
async def get_users_me(
    current_user: contract.User = Depends(user_crud.get_current_user),
):
    current_user = dict(current_user)
    respond = contract.User(
        name=current_user["name"],
        login=current_user["login"],
        # image
    )
    return respond
