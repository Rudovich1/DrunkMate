from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from google.auth.transport import requests
from google.oauth2 import id_token
from pydantic import EmailStr

from drunkMate.api.auth import contract
from drunkMate.core import repository
from drunkMate.core.cruds import user_crud
from drunkMate.startup import initialization

router = APIRouter()


@router.on_event("startup")
async def startup():
    await initialization.initialization()


@router.post("/auth_api/registration", response_model=contract.Token)
async def create_new_user(user_registration: contract.UserRegistration):
    if repository.get_user(user_registration.login):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this login already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_registration_dict = user_registration.dict()
    user_registration_dict['role'] = repository.Role.USER.value
    await user_crud.create_user(user_registration_dict)
    access_token = user_crud.create_access_token(data={"sub": user_registration.login})
    respond = contract.Token(access_token=access_token, token_type="bearer")
    # respond = contract.Token(accessToken=access_token, tokenType="bearer")
    return respond


@router.post("/auth_api/login", response_model=contract.Token)
@router.post("/token", response_model=contract.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_inwork = user_crud.authenticate_user(
        EmailStr(form_data.username), form_data.password
    )
    if not user_inwork:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = user_crud.create_access_token(data={"sub": user_inwork["login"]})
    response = contract.Token(access_token=access_token, token_type="Bearer")
    # response = contract.Token(accessToken=access_token, tokenType="Bearer") - for node client
    return response


@router.post("/auth_api/swap_tokens/google")
async def swap_token_from_external_provider(credentials: contract.GoogleOAuthCredentials):
    id_info = id_token.verify_oauth2_token(
        credentials.token,
        requests.Request(),
        credentials.client_id,
    )
    user = repository.get_user(id_info['email'])
    if user is not None:
        usr = {
            "login": id_info["email"],
            "name": id_info["name"],
            "hashed_password": None,
            "role": 0
        }
        repository.add_user(usr)
    access_token = user_crud.create_access_token(data={"sub": id_info["email"]})
    respond = contract.Token(access_token=access_token, token_type="bearer")
    return respond

    # user_registration_dict = user_registration.dict()
    # user_registration_dict['role'] = repository.Role.USER.value
    # await user_crud.create_user(user_registration_dict)
    # access_token = user_crud.create_access_token(data={"sub": user_registration.login})
    # respond = contract.Token(access_token=access_token, token_type="bearer")
    # return respond
