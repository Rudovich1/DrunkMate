from drunkMate.core import repository
from bson.objectid import ObjectId
from fastapi import HTTPException, status


async def get_cocktail(cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)
    if cocktail is None:
        return None
    return {'id': str(cocktail['_id']),
            'name': cocktail['name'],
            'description': cocktail['description'],
            'rating': cocktail['rating'],
            'tags': cocktail['tags'],
            'recipe': cocktail['recipe'],
            'author': str(cocktail['author']),
            'strength': cocktail['strength'],
            'ingredients': list(cocktail['ingredients']),
            'comments': list(map(lambda x: str(x), cocktail['comments'])),
            'parent_cocktails': cocktail['parent_cocktails']}


async def post_cocktail(item: dict, author_id: str):
    cocktail = {
        'name': item['name'],
        'description': item['description'],
        'rating': None,
        'tags': item['tags'],
        'recipe': item['recipe'],
        'author': ObjectId(author_id),
        'strength': item['strength'],
        'ingredients': item['ingredients'],
        'comments': [],
        'parent_cocktails': item['parent_cocktails'] 
    }
    
    for ingredient in item['ingredients']:
        if (repository.get_ingredient(ingredient['name']) is None):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There are no declared ingredients",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    repository.post_cocktail(cocktail)
    
    for tag in item['tags']:
        repository.post_tag({'name': tag})
    
    
async def get_cocktails():
    cocktails = list(repository.get_cocktails())
    res_cocktails = []
    for cocktail in cocktails:
        res_cocktails.append({  'id': str(cocktail['_id']),
                                'name': cocktail['name'],
                                'rating': cocktail['rating'],
                                'tags': cocktail['tags'],
                                'author': str(cocktail['author']),
                                'strength': cocktail['strength']})
        
    return res_cocktails


async def put_cocktail(cocktail_id: str, item: dict):
    
    item = {'name': item['name'],
            'description': item['description'],
            'tags': item['tags'],
            'recipe': item['recipe'],
            'strength': item['strength'],
            'ingredients': item['ingredients'],
            'parent_cocktails': item['parent_cocktails'] }
    
    if repository.put_cocktail(cocktail_id, item) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The cocktail does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    for tag in item['tags']:
        repository.post_tag({'name': tag})


async def delete_cocktail(cocktail_id: str):
    
    cocktail = repository.get_cocktail(cocktail_id)
    
    if cocktail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The cocktail does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    for comment in cocktail['comments']:
        repository.delete_comment(str(comment))
    
    repository.delete_cocktail(cocktail_id)
    
    
async def get_cocktails_by_tags(tags: list[str]):
    
    cocktails = repository.get_cocktails()
    res_cocktails = []
    
    for cocktail in cocktails:
        for tag in tags:
            if tag not in cocktail['tags']:
                break
        else:
            res_cocktails.append(str(cocktail['_id']))
                
    return res_cocktails


async def get_cocktails_by_ingredients(ingredients: list[str]):
    
    cocktails = repository.get_cocktails()
    res_cocktails = []
    
    for cocktail in cocktails:
        cocktail_ingredients = []
        for cocktail_ingredient in cocktail['ingredients']:
            cocktail_ingredients.append(cocktail_ingredient['name'])
                
        for ingredient in ingredients:
            if ingredient not in cocktail_ingredients:
                break
        else:
            res_cocktails.append(str(cocktail['_id']))
                
    return res_cocktails
