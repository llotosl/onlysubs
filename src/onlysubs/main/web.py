from fastapi import FastAPI

from onlysubs.main.di import init_dependencies
from onlysubs.main.exceptions import setup_exception_handlers
from onlysubs.main.routers import init_routers


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_dependencies(app)
    setup_exception_handlers(app)
    return app
