import logging

import uvicorn
from fastapi import FastAPI

from src.main.di import init_dependencies
from src.main.exceptions import setup_exception_handlers
from src.main.routers import init_routers

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI()
    init_routers(app)
    init_dependencies(app)
    setup_exception_handlers(app)
    return app


async def run_uvicorn_api(app: FastAPI) -> None:
    config = uvicorn.Config(
        app,
        host="127.0.0.1",
        port=8000,
        log_level=logging.INFO,
        log_config="logging.ini",
    )
    server = uvicorn.Server(config)
    logger.info("Running API")
    await server.serve()


async def main() -> None:
    app = create_app()
    await run_uvicorn_api(app)
