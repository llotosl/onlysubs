from typing import Annotated
from fastapi import APIRouter, Depends
from onlysubs.application.register_user.dto import RegisterUserDTO
from onlysubs.application.register_user.use_case import RegisterUser
from onlysubs.domain.models.user import User

from onlysubs.presentation.fapi.stub import Stub

users_router = APIRouter(prefix="/users")


@users_router.post("", response_model=User)
async def register_user_route(
    data: RegisterUserDTO,
    register_user: Annotated[RegisterUser, Depends(Stub(RegisterUser))],
) -> User:
    return await register_user(data)
