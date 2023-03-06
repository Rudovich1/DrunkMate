from tag import Tag


class Ingredient(object):
    def __init__(self, id: str, name: str, tags: list[Tag], description: str):
        self.id = id
        self.name = name
        self.tags = tags
        self.description = description
