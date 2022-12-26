from drunkMate.core import repository
from drunkMate.core.cruds import tag_crud


async def post_ingredient(item: dict):
    for tag in item['tags']:
        repository.post_tag({'name': tag}, is_ingredient=True)
        
    repository.post_ingredient(item)


async def get_ingredients():
    ingredients = repository.get_ingredients()
    print(ingredients)
    resp = []
    for item in ingredients:
        print(tag_crud.get_tags(is_ingredient=True, ids=list(map(lambda x: str(x), item['tags']))))
        item['tags'] = list(await tag_crud.get_tags(is_ingredient=True, ids=list(item['tags'])))
        item = {'name': item['name'], 'description': item['description'], 'tags': item['tags']}
        resp.append(item)
    return resp


async def put_ingredient(item: dict):
    repository.put_ingredient(item['old_name'], {'name': item['name'], 'description': item['description'], 'tags': item['tags']})
    

async def delete_ingredient(ingredient_name: str):
    repository.delete_ingredient(ingredient_name)