from bson.objectid import ObjectId
from enum import Enum

from drunkMate.service.db.mongo import database
from drunkMate.models import user

drunkMate_db = database.get_database(database.DBSettings())


class Role(Enum):
    USER = 0
    DRUNKMASTER = 1


class Strength(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    STRONG = 3


# --------------------------------USER--------------------------------


def get_user(login: str, db=drunkMate_db):
    users_collection = db["users_collection"]
    respond = users_collection.find_one({"login": login})
    if respond:
        respond = dict(respond)
    return respond


def add_user(item: dict, db=drunkMate_db):
    usr = user.User(
        login=item["login"],
        name=item["name"],
        hashed_password=item["hashed_password"],
        # image=,
        role=Role.USER.value
    )
    users_collection = db["users_collection"]
    users_collection.insert_one(usr.dict())


# --------------------------------COCKTAIL--------------------------------


def get_cocktail(cocktail_id: str, db=drunkMate_db):
    try:
        cocktail_id = ObjectId(cocktail_id)
        cocktail_collection = db["cocktails_collection"]
        cocktail = cocktail_collection.find_one({"_id": cocktail_id})
    except:
        cocktail = None
    return cocktail


# --------------------------------INGREDIENT--------------------------------


def create_ingredient(item: dict, db=drunkMate_db):
    collection = db["ingredients_collection"]
    resp = collection.find_one({'name': item['name']})
    if resp is None:
        collection.insert_one(item)


def get_ingredients(db=drunkMate_db):
    collection = db["ingredients_collection"]
    return list(collection.find())


# --------------------------------TAG--------------------------------


def create_tag(item: dict, is_ingredient: bool, db=drunkMate_db):
    if is_ingredient:
        collection = db["ingredient_tags_collection"]
    else:
        collection = db["cocktail_tags_collection"]
    collection.update_one(filter={'name': item['name']}, update={'$set': item}, upsert=True)


def get_tags(is_ingredient: bool, ids: list=None, db=drunkMate_db):
    if is_ingredient:
        collection = db["ingredient_tags_collection"]
    else:
        collection = db["cocktail_tags_collection"]
    if ids is None:
        resp = collection.find()
    else:
        resp = collection.find({"_id": {"$in": ids}})
    return list(resp)