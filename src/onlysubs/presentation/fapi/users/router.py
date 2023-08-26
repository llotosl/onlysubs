from typing import Annotated
from fastapi import APIRouter, Depends
from onlysubs.application.activate_user.dto import ActivateUserDTO
from onlysubs.application.activate_user.use_case import ActivateUser
from onlysubs.application.register_user.dto import RegisterUserDTO
from onlysubs.application.register_user.use_case import RegisterUser
from onlysubs.domain.models.user import User
from onlysubs.presentation.fapi.users.models import ActivateUserModel


users_router = APIRouter()


@users_router.post("", response_model=User)
async def register_user_route(
    data: RegisterUserDTO,
    register_user: Annotated[RegisterUser, Depends()],
) -> User:
    return await register_user(data)


@users_router.post("/activate", response_model=None)
async def activate_user_route(
    data: ActivateUserModel,
    activate_user: Annotated[ActivateUser, Depends()],
) -> None:
    return await activate_user(
        ActivateUserDTO(
            activation_token=data.activation_token,
        ),
    )
