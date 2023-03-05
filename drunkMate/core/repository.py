from bson.objectid import ObjectId
from enum import Enum

from drunkMate.service.db.mongo import database
from drunkMate.service.db.models import user

drunkMate_db = database.get_database(database.DBSettings())


class Role(Enum):
    USER = 0
    DRUNKMASTER = 1


class Strength(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    STRONG = 3


class UnitType(Enum):
    MILLILITERS = 0
    GRAMS = 1
    UNITS = 2


# --------------------------------USER--------------------------------


def get_user(login: str, db=drunkMate_db):
    users_collection = db["users"]
    respond = users_collection.find_one({"login": login})
    if respond:
        respond = dict(respond)
    return respond


def get_user_by_id(id: ObjectId, db = drunkMate_db):
    users_collection = db["users"]
    respond = users_collection.find_one({"_id": id})
    if respond:
        respond = dict(respond)
    return respond


def add_user(item: dict, db=drunkMate_db):
    usr = user.User(
        login=item["login"],
        name=item["name"],
        hashed_password=item["hashed_password"],
        # image=,
        role=item["role"]
    )
    users_collection = db["users"]
    users_collection.insert_one(usr.dict())


# --------------------------------COCKTAIL--------------------------------


def post_cocktail(item: dict,  db=drunkMate_db):
    collection = db['cocktails']
    return collection.insert_one(item)


def get_cocktail(cocktail_id: str, db=drunkMate_db):
    try:
        cocktail_id = ObjectId(cocktail_id)
        cocktail_collection = db["cocktails"]
        cocktail = cocktail_collection.find_one({"_id": cocktail_id})
    except:
        cocktail = None
    return cocktail


def get_cocktails(search=None, tags=None, ingredients=None, db=drunkMate_db):
    search = str(f"/*{search}/*") if search and len(search) > 0 else "/*"
    cocktails = db['cocktails'].find({
            "name": {"$regex": search, "$options": "i"},
            "tags": {"$all": {"$in": tags}, "$options": "i"},
            "ingredients": {
                "name": {"$all": {"$in": ingredients}, "$options": "i"}
            }
        }
    )

    return cocktails


def put_cocktail(cocktail_id: str, item: dict, db=drunkMate_db):
    collection = db['cocktails']
    return collection.update_one({'_id': ObjectId(cocktail_id)}, {'$set': item})
    
    
def delete_cocktail(cocktail_id: str, db=drunkMate_db):
    collection = db['cocktails']
    collection.delete_one(filter={'_id': ObjectId(cocktail_id)})
    

# --------------------------------INGREDIENT--------------------------------


def post_ingredient(item: dict, db=drunkMate_db):
    collection = db["ingredients"]
    resp = collection.find_one({'name': item['name']})
    if resp is None:
        collection.insert_one(item)


def get_ingredients(db=drunkMate_db):
    collection = db["ingredients"]
    return list(collection.find())


def put_ingredient(old_name: str, item: dict, db=drunkMate_db):
    collection = db["ingredients"]
    collection.update_one(filter={'name': old_name}, update={'$set': item})
        

def delete_ingredient(ingredient_name: str, db=drunkMate_db):
    collection = db["ingredients"]
    collection.delete_one({'name': ingredient_name})


def get_ingredient(name: str, db=drunkMate_db):
    collection = db["ingredients"]
    return collection.find_one({'name': name})
    
# --------------------------------TAG--------------------------------


def post_tag(item: dict, is_ingredient: bool = False, db=drunkMate_db):
    if is_ingredient:
        collection = db["ingredient_tags"]
    else:
        collection = db["cocktail_tags"]
    collection.update_one(filter={'name': item['name']}, update={'$set': item}, upsert=True)


def get_tags(is_ingredient: bool, ids: list=None, db=drunkMate_db):
    if is_ingredient:
        collection = db["ingredient_tags"]
    else:
        collection = db["cocktail_tags"]
    if ids is None:
        resp = collection.find()
    else:
        resp = collection.find({"_id": {"$in": ids}})
    return resp


def delete_tag(is_ingredient: bool, tag_name: str, db=drunkMate_db):
    if is_ingredient:
        collection = db['ingredient_tags']
    else:
        collection = db['cocktail_tags']
    collection.delete_one({'name': tag_name})
    
    
def get_tag(is_ingredient: bool, name: str, db=drunkMate_db):
    if is_ingredient:
        collection = db["ingredient_tags"]
    else:
        collection = db["cocktail_tags"]
        
    return collection.find_one({'name': name})


# --------------------------------COMMENT--------------------------------


def post_comment(author_id: str, text: str, rating: int, db=drunkMate_db):
    collection = db["comments"]
    elem = collection.insert_one({'author': ObjectId(author_id), 'text': text, 'rating': rating})
    return str(elem.inserted_id)


def put_comment(comment_id: str, text: str, rating: int, db=drunkMate_db):
    collection = db['comments']
    collection.update_one({'_id': comment_id}, {'$set': {'text': text, 'rating': rating}})


def get_comment(comment_id: str, db=drunkMate_db):
    collection = db['comments']
    return collection.find_one({'_id': ObjectId(comment_id)})


def get_comments(cocktail_id: str, db=drunkMate_db):
    collection = db['comments']
    cocktail = get_cocktail(cocktail_id, db)
    if cocktail is None:
        return None
    comments_ids = cocktail['comments']
    collection = db['comments']
    comments = list(collection.find(filter={'_id': {"$in": comments_ids}}))
    return comments


def delete_comment(comment_id: str, db=drunkMate_db):
    collection = db['comments']
    collection.delete_one({'_id': ObjectId(comment_id)})
