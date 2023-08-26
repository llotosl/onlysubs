from typing import Annotated
from fastapi import APIRouter, Depends
from onlysubs.application.activate_user.dto import ActivateUserDTO
from onlysubs.application.activate_user.use_case import ActivateUser
from onlysubs.application.register_user.dto import RegisterUserDTO
from onlysubs.application.register_user.use_case import RegisterUser
from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import User, Username
from onlysubs.domain.models.user_activation import UserActivationToken
from onlysubs.presentation.fapi.users.models import (
    ActivateUserModel,
    PublicUserModel,
    RegisterUserModel,
)


users_router = APIRouter()


@users_router.post("", response_model=PublicUserModel)
async def register_user_route(
    data: RegisterUserModel,
    register_user: Annotated[RegisterUser, Depends()],
) -> User:
    return await register_user(
        RegisterUserDTO(
            email=Email(data.email),
            first_name=data.first_name,
            last_name=data.last_name,
            username=Username(data.username),
            password=data.password,
        ),
    )


@users_router.post("/activate", response_model=None)
async def activate_user_route(
    data: ActivateUserModel,
    activate_user: Annotated[ActivateUser, Depends()],
) -> None:
    return await activate_user(
        ActivateUserDTO(
            activation_token=UserActivationToken(data.activation_token),
        ),
    )
