from drunkMate.core import repository
from fastapi import HTTPException, status


async def post_tag(tag_data: dict, is_ingredient=False):
    
    if repository.get_tag(is_ingredient, tag_data['name']) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The tag already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return repository.post_tag(tag_data, is_ingredient=is_ingredient)  


async def get_tags(search="", is_ingredient=False, ids: list=None):
    resp = list(repository.get_tags(search, is_ingredient, ids))
    names = []
    for item in resp:
        names.append(item['name'])
    return names


async def delete_tag(tag_name: str, is_ingredient=False):
    
    if repository.get_tag(is_ingredient, tag_name) is None:
        raise HTTPException(
            status_code=status.HTTP_404_BAD_REQUEST,
            detail="The tag does not exist",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if is_ingredient:
        ings = repository.get_ingredients()
        for ing in ings:
            tags = ing['tags']
            if tag_name in tags:
                tags.remove(tag_name)
                repository.put_ingredient(ing['name'], {'tags': tags})
    else:
        cocks = repository.get_cocktails()
        for cock in cocks:
            tags = cock['tags']
            if tag_name in tags:
                tags.remove(tag_name)
                repository.put_cocktail(str(cock['_id']), {'tags': tags})
    
    
    repository.delete_tag(is_ingredient, tag_name)