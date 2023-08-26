from datetime import timedelta
from logging import getLogger

from fastapi import FastAPI, Depends

from onlysubs.adapters.db.in_memory.uow import InMemoryUoW
from onlysubs.adapters.db.in_memory.user import InMemoryUserRepository
from onlysubs.adapters.emails.stdout.email_sender import StdoutEmailSender
from onlysubs.application.activate_user.interfaces import (
    EmailSender as ActivateUserEmailSender,
    UserRepository as ActivateUserUserRepository,
)
from onlysubs.application.activate_user.use_case import ActivateUser, ActivateUserImpl
from onlysubs.application.common.interfaces.uow import UoW
from onlysubs.application.register_user.interfaces import (
    EmailSender as RegisterUserEmailSender,
    UserRepository as RegisterUserUserRepository,
)
from onlysubs.application.register_user.use_case import RegisterUser, RegisterUserImpl
from onlysubs.application.resend_activation_email.use_case import (
    ResendActivationEmail,
    ResendActivationEmailImpl,
)
from onlysubs.domain.services.user import UserService
from onlysubs.domain.services.user_activation import UserActivationService

from onlysubs.application.resend_activation_email.interfaces import (
    UserRepository as ResendActivationEmailUserRepository,
    EmailSender as ResendActivationEmailEmailSender,
)

logger = getLogger(__name__)


def all_depends(cls: type) -> None:
    """
    Adds `Depends()` to the class `__init__` methods, so it can be used
    a fastapi dependency having own dependencies
    """
    init = cls.__init__
    total_ars = init.__code__.co_kwonlyargcount + init.__code__.co_argcount - 1
    init.__defaults__ = tuple(Depends() for _ in range(total_ars))


def new_uow() -> InMemoryUoW:
    return InMemoryUoW()


def new_email_sender() -> StdoutEmailSender:
    return StdoutEmailSender()


def new_user_repo() -> InMemoryUserRepository:
    return InMemoryUserRepository()


def new_user_service() -> UserService:
    return UserService("PASSWORD_SALT")


def new_user_activation_service() -> UserActivationService:
    return UserActivationService(
        "SECRET_KEY",
        "HS256",
        timedelta(days=7),
    )


def init_dependencies(app: FastAPI) -> None:
    app.dependency_overrides[UoW] = new_uow

    app.dependency_overrides[UserService] = new_user_service
    app.dependency_overrides[UserActivationService] = new_user_activation_service

    app.dependency_overrides[ActivateUserEmailSender] = new_email_sender
    app.dependency_overrides[ActivateUserUserRepository] = new_user_repo

    app.dependency_overrides[RegisterUserEmailSender] = new_email_sender
    app.dependency_overrides[RegisterUserUserRepository] = new_user_repo

    app.dependency_overrides[ResendActivationEmailEmailSender] = new_email_sender
    app.dependency_overrides[ResendActivationEmailUserRepository] = new_user_repo

    all_depends(RegisterUserImpl)
    all_depends(ActivateUserImpl)
    all_depends(ResendActivationEmailImpl)

    app.dependency_overrides[RegisterUser] = RegisterUserImpl
    app.dependency_overrides[ActivateUser] = ActivateUserImpl
    app.dependency_overrides[ResendActivationEmail] = ResendActivationEmailImpl
