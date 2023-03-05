from drunkMate.core import repository
from drunkMate.core.cruds import cocktail_crud
from fastapi import HTTPException, status

async def post_ingredient(item: dict):
    
    if repository.get_ingredient(item['name']) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The ingredient already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    repository.post_ingredient(item)
    
    for tag in item['tags']:
        repository.post_tag({'name': tag}, is_ingredient=True)


async def get_ingredients(search = "", tags = []):
    ingredients = repository.get_ingredients(search, tags)
    resp = []
    for item in ingredients:
        item = {'id': str(item['_id']), 'name': item['name'], 'description': item['description'], 'tags': item['tags']}
        resp.append(item)
    return resp


async def put_ingredient(item: dict):
    
    if repository.get_ingredient(item['name']) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TThe ingredient does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    for tag in item['tags']:
        repository.post_tag({'name': tag}, is_ingredient=True)
        
    repository.put_ingredient(item['old_name'], {'name': item['name'], 'description': item['description'], 'tags': item['tags']})
    

async def delete_ingredient(ingredient_name: str):
    
    if repository.get_ingredient(ingredient_name) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The ingredient does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    for cocktail in await cocktail_crud.get_cocktails(ingredients=[ingredient_name]):
        await cocktail_crud.delete_cocktail(cocktail['id'])
    
    repository.delete_ingredient(ingredient_name)

