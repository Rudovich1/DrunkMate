from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .endpoints import router


def bootstrap(app: FastAPI) -> FastAPI:
    app.include_router(router)
    origins = [
        "http://localhost:3000",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )
    return app
