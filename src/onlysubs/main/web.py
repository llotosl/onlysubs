from fastapi import FastAPI

from onlysubs.main.di import init_dependencies
from onlysubs.main.routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_dependencies(app)
    return app
