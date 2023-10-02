from typing import Annotated

from fastapi import APIRouter, Depends

from onlysubs.application.activate_user.dto import ActivateUserDTO
from onlysubs.application.activate_user.use_case import ActivateUser
from onlysubs.application.register_user.dto import RegisterUserDTO
from onlysubs.application.register_user.use_case import RegisterUser
from onlysubs.application.resend_activation_email.dto import (
    ResendActivationEmailDTO,
)
from onlysubs.application.resend_activation_email.use_case import (
    ResendActivationEmail,
)
from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import User, Username
from onlysubs.domain.models.user_activation import UserActivationToken
from onlysubs.presentation.fapi.users.models import (
    ActivateUserModel,
    PublicUserModel,
    RegisterUserModel,
    ResendActivationEmailModel,
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


@users_router.post("/activation", response_model=None)
async def activate_user_route(
    data: ActivateUserModel,
    activate_user: Annotated[ActivateUser, Depends()],
) -> None:
    return await activate_user(
        ActivateUserDTO(
            activation_token=UserActivationToken(data.activation_token),
        ),
    )


@users_router.post("/activation/resend", response_model=None)
async def resend_activation_email_route(
    data: ResendActivationEmailModel,
    resend_activation_email: Annotated[ResendActivationEmail, Depends()],
) -> None:
    return await resend_activation_email(
        ResendActivationEmailDTO(
            user_email=Email(data.email),
        ),
    )
