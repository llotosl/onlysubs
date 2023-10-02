from fastapi import FastAPI

from src.presentation.fapi.root import root_router


def init_routers(app: FastAPI) -> None:
    app.include_router(root_router)
