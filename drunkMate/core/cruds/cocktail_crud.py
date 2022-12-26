from drunkMate.core import repository
from bson.objectid import ObjectId



async def get_cocktail(cocktail_id: str):
    cocktail = repository.get_cocktail(cocktail_id)

    return cocktail


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
    
    for tag in item['tags']:
        repository.post_tag({'name': tag})
    
    repository.post_cocktail(cocktail)
    
    
async def get_cocktails():
    cocktails = list(repository.get_cocktails())
    res_cocktails = []
    for cocktail in cocktails:
        res_cocktails.append({'name': cocktail['name'],
                                'description': cocktail['description'],
                                'rating': cocktail['rating'],
                                'tags': cocktail['tags'],
                                'recipe': cocktail['recipe'],
                                'author': str(cocktail['author']),
                                'strength': cocktail['strength'],
                                'ingredients': cocktail['ingredients'],
                                'comments': cocktail['comments'],
                                'parent_cocktails': cocktail['parent_cocktails'] })
        
    return res_cocktails


async def put_cocktail(cocktail_id: str, item: dict):
    
    item = {'name': item['name'],
            'description': item['description'],
            'tags': item['tags'],
            'recipe': item['recipe'],
            'strength': item['strength'],
            'ingredients': item['ingredients'],
            'parent_cocktails': item['parent_cocktails'] }
    
    repository.put_cocktail(cocktail_id, item)
    
    for tag in item['tags']:
        repository.post_tag({'name': tag})
    

async def delete_cocktail(cocktail_id: str):
    
    cocktail = repository.get_cocktail(cocktail_id)
    
    for comment in cocktail['comments']:
        repository.delete_comment(comment['_id'])
    
    repository.delete_cocktail(cocktail_id)