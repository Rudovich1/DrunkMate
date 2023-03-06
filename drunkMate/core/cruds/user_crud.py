from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from drunkMate.service.db.models import settings
from drunkMate.core.token import TokenData
from drunkMate.core import repository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

my_settings = settings.Settings()


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(login: str, password: str):
    user_inwork = repository.get_user(login)
    if not user_inwork:
        return False
    if not verify_password(password, user_inwork.get("hashed_password")):
        return False
    return user_inwork


def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(
        to_encode, my_settings.secret_key, algorithm=my_settings.algorithm
    )
    return encoded_jwt


async def create_user(user_registration: dict):
    user_registration["hashed_password"] = get_password_hash(
        user_registration["password"]
    )
    repository.add_user(user_registration)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"www-authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, my_settings.secret_key, algorithms=my_settings.algorithm
        )
        login: str = payload.get("sub")
        if login is None:
            raise credentials_exception
        token_data = TokenData(login=login)
    except JWTError:
        raise credentials_exception
    user = repository.get_user(login=token_data.login)
    if user is None:
        raise credentials_exception
    return user
