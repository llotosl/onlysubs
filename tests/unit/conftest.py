from datetime import timedelta

import pytest

from onlysubs.adapters.activation_crypt.jwt_crypt.jwt_cryptor import (
    JWTActivationCryptor,
)
from onlysubs.adapters.db.in_memory.uow import InMemoryUoW
from onlysubs.adapters.db.in_memory.user import InMemoryUserRepository
from onlysubs.adapters.emails.stdout.email_sender import StdoutEmailSender
from onlysubs.application.activate_user.use_case import ActivateUserImpl
from onlysubs.application.register_user.use_case import RegisterUserImpl
from onlysubs.domain.services.user import UserService
from onlysubs.domain.services.user_activation import UserActivationService


@pytest.fixture()
def in_memory_user_repository() -> InMemoryUserRepository:
    return InMemoryUserRepository()


@pytest.fixture()
def user_activation_service() -> UserActivationService:
    return UserActivationService(activity_delta=timedelta(minutes=60))


@pytest.fixture()
def in_memory_uow() -> InMemoryUoW:
    return InMemoryUoW()


@pytest.fixture()
def stdout_email_sender() -> StdoutEmailSender:
    return StdoutEmailSender()


@pytest.fixture()
def jwt_cryptor() -> JWTActivationCryptor:
    return JWTActivationCryptor("test", "HS256")


@pytest.fixture()
def activate_user_use_case(
    in_memory_user_repository: InMemoryUserRepository,
    user_activation_service: UserActivationService,
    in_memory_uow: InMemoryUoW,
    stdout_email_sender: StdoutEmailSender,
    jwt_cryptor: JWTActivationCryptor,
) -> ActivateUserImpl:
    return ActivateUserImpl(
        in_memory_user_repository,
        user_activation_service,
        stdout_email_sender,
        in_memory_uow,
        jwt_cryptor,
    )


@pytest.fixture()
def user_service() -> UserService:
    return UserService()


@pytest.fixture()
def register_user_use_case(
    in_memory_user_repository: InMemoryUserRepository,
    user_activation_service: UserActivationService,
    in_memory_uow: InMemoryUoW,
    stdout_email_sender: StdoutEmailSender,
    jwt_cryptor: JWTActivationCryptor,
    user_service: UserService,
) -> RegisterUserImpl:
    return RegisterUserImpl(
        in_memory_user_repository,
        user_service,
        user_activation_service,
        stdout_email_sender,
        in_memory_uow,
        jwt_cryptor,
    )
