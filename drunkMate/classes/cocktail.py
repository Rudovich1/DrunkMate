from enum import Enum

from ingredient import Ingredient
from comment import Comment
from user import User
from tag import Tag


class Strength(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    STRONG = 3


class UnitType(Enum):
    MILLILITERS = 0
    GRAMS = 1
    UNITS = 2


class _IngredientWrapper(object):
    def __init__(self, ingredient: Ingredient, amount: int, unit: UnitType):
        self.ingredient = ingredient
        self.amount = amount
        self.unit = unit


class Cocktail(object):
    def __inti__(
        self,
        id: str,
        name: str,
        description: str,
        rating: float,
        tags: list[Tag],
        recipe: str,
        author: User,
        strength: Strength,
        ingredient_wrappers: list[_IngredientWrapper],
        comments: list[Comment],
        parent_cocktails: list,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.rating = rating
        self.tags = tags
        self.recipe = recipe
        self.author = author
        self.strength = strength
        self.ingredient_wrappers = ingredient_wrappers
        self.comments = comments
        self.parent_cocktails = parent_cocktails
