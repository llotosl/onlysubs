from fastapi import APIRouter

from src.presentation.fapi.avatars.router import avatar_router
from src.presentation.fapi.index import index_router
from src.presentation.fapi.users.router import users_router

root_router = APIRouter()
root_router.include_router(
    users_router,
    prefix="/users",
)
root_router.include_router(
    index_router,
)
root_router.include_router(avatar_router, prefix="/avatar")
