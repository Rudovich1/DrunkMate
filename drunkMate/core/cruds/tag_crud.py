from drunkMate.core import repository


async def create_tag(tag_data: dict, is_ingredient=False):
    repository.create_tag(tag_data, is_ingredient=is_ingredient)


async def get_tags(is_ingredient=False, ids: list=None):
    resp = repository.get_tags(is_ingredient=is_ingredient, ids=ids)
    ids = list(map(lambda x: str(x['_id']), resp))
    names = list(map(lambda x: x['name'], resp))
    resp = zip(ids, names)
    return resp
