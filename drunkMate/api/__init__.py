import toolz
from fastapi import FastAPI

from . import auth, user, cocktail, tag, ingredient, comment


def create_app() -> FastAPI:
    return toolz.pipe(
        FastAPI(),
        auth.bootstrap,
        user.bootstrap,
        cocktail.bootstrap,
        tag.bootstrap,
        ingredient.bootstrap,
        comment.bootstrap,
    )
