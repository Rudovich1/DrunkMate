import pymongo.database
from pydantic import BaseSettings, MongoDsn, Field
from pymongo import MongoClient


class DBSettings(BaseSettings):
    connection_string: MongoDsn = Field(env="DB_CONNECTION_STRING")


def get_database(db_settings: DBSettings) -> pymongo.database.Database:
    client = MongoClient(db_settings.connection_string)
    db = client["drunkMate_database"]
    return db
