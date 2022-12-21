from drunkMate.core import repository
from drunkMate.core.cruds import tag_crud


async def create_ingredient(item: dict):
    repository.create_ingredient(item)


async def get_ingredients():
    resp = repository.get_ingredients()
    for item in resp:
        item['tags'] = list(await tag_crud.get_tags(is_ingredient=True, ids=list(map(lambda x: str(x), item['tags']))))
    return resp
