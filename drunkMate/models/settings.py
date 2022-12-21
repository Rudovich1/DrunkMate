from pydantic import BaseSettings


class Settings(BaseSettings):
    algorithm: str
    secret_key: str
