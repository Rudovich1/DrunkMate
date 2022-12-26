from drunkMate.core import repository


async def post_tag(tag_data: dict, is_ingredient=False):
    return repository.post_tag(tag_data, is_ingredient=is_ingredient)  


async def get_tags(is_ingredient=False, ids: list=None):
    resp = list(repository.get_tags(is_ingredient=is_ingredient, ids=ids))
    names = []
    for item in resp:
        names.append(item['name'])
    return names


async def delete_tag(tag_name: str, is_ingredient=False):
    
    if is_ingredient:
        ings = repository.get_ingredients()
        for ing in ings:
            tags = ing['tags']
            if tags.find(tag_name):
                tags.remove(tag_name)
                repository.put_ingredient(ing['name'], {'tags': tags})
    
    repository.delete_tag(is_ingredient, tag_name)