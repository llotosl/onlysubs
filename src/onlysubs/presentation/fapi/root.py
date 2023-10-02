from fastapi import APIRouter

from onlysubs.presentation.fapi.index import index_router
from onlysubs.presentation.fapi.users.router import users_router
from onlysubs.presentation.fapi.avatars.router import avatar_router

root_router = APIRouter()
root_router.include_router(
    users_router,
    prefix="/users",
)
root_router.include_router(
    index_router,
)
root_router.include_router(avatar_router, prefix="/avatar")
