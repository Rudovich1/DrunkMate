from drunkMate.core import repository


async def post_tag(tag_data: dict, is_ingredient=False):
    return repository.post_tag(tag_data, is_ingredient=is_ingredient)  


async def get_tags(is_ingredient=False, ids: list=None):
    resp = repository.get_tags(is_ingredient=is_ingredient, ids=ids)
    print(resp)
    names = list(map(lambda x: x['name'], resp))
    print(names)
    return names

async def delete_tag(tag_name: str, is_ingredient=False):
    repository.delete_tag(is_ingredient, tag_name)