from datetime import timedelta
from logging import getLogger

from fastapi import Depends, FastAPI
from onlysubs.adapters.db.in_memory.avatar import InMemoryAvatarRepository
from onlysubs.adapters.db.in_memory.file import InMemoryFileRepository

from onlysubs.adapters.db.in_memory.uow import InMemoryUoW
from onlysubs.adapters.db.in_memory.user import InMemoryUserRepository
from onlysubs.adapters.emails.stdout.email_sender import StdoutEmailSender
from onlysubs.adapters.storage.local.file import LocalFileStorageGateway
from onlysubs.application.activate_user.interfaces import (
    EmailSender as ActivateUserEmailSender,
)
from onlysubs.application.activate_user.interfaces import (
    UserRepository as ActivateUserUserRepository,
)
from onlysubs.application.activate_user.use_case import ActivateUser, ActivateUserImpl
from onlysubs.application.add_avatar_to_user.interfaces import (
    FileRepository as AddAvatarToUserFileRepository,
    FileStorageGateway as AddAvatarToUserFileStorageGateway,
    UserAvatarRepository as AddAvatarToUserUserAvatarRepository,
    UserRepository as AddAvatarToUserUserRepository,
)
from onlysubs.application.add_avatar_to_user.use_case import (
    AddAvatarToUser,
    AddAvatarToUserImpl,
)
from onlysubs.application.common.interfaces.uow import UoW
from onlysubs.application.register_user.interfaces import (
    EmailSender as RegisterUserEmailSender,
)
from onlysubs.application.register_user.interfaces import (
    UserRepository as RegisterUserUserRepository,
)
from onlysubs.application.register_user.use_case import RegisterUser, RegisterUserImpl
from onlysubs.application.resend_activation_email.interfaces import (
    EmailSender as ResendActivationEmailEmailSender,
)
from onlysubs.application.resend_activation_email.interfaces import (
    UserRepository as ResendActivationEmailUserRepository,
)
from onlysubs.application.resend_activation_email.use_case import (
    ResendActivationEmail,
    ResendActivationEmailImpl,
)
from onlysubs.domain.services.avatar import UserAvatarService
from onlysubs.domain.services.file import FileService
from onlysubs.domain.services.user import UserService
from onlysubs.domain.services.user_activation import UserActivationService

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


def new_file_service() -> FileService:
    return FileService()


def new_avatar_service() -> UserAvatarService:
    return UserAvatarService()


def new_file_repo() -> InMemoryFileRepository:
    return InMemoryFileRepository()


def new_avatar_repo() -> InMemoryAvatarRepository:
    return InMemoryAvatarRepository()


def new_file_storage_gateway() -> LocalFileStorageGateway:
    return LocalFileStorageGateway()


def init_dependencies(app: FastAPI) -> None:
    app.dependency_overrides[UoW] = new_uow

    app.dependency_overrides[UserService] = new_user_service
    app.dependency_overrides[UserActivationService] = new_user_activation_service
    app.dependency_overrides[FileService] = new_file_service
    app.dependency_overrides[UserAvatarService] = new_avatar_service

    app.dependency_overrides[ActivateUserEmailSender] = new_email_sender
    app.dependency_overrides[ActivateUserUserRepository] = new_user_repo

    app.dependency_overrides[RegisterUserEmailSender] = new_email_sender
    app.dependency_overrides[RegisterUserUserRepository] = new_user_repo

    app.dependency_overrides[ResendActivationEmailEmailSender] = new_email_sender
    app.dependency_overrides[ResendActivationEmailUserRepository] = new_user_repo

    app.dependency_overrides[AddAvatarToUserFileRepository] = new_file_repo
    app.dependency_overrides[AddAvatarToUserUserRepository] = new_user_repo
    app.dependency_overrides[AddAvatarToUserUserAvatarRepository] = new_avatar_repo
    app.dependency_overrides[
        AddAvatarToUserFileStorageGateway
    ] = new_file_storage_gateway

    all_depends(RegisterUserImpl)
    all_depends(ActivateUserImpl)
    all_depends(ResendActivationEmailImpl)
    all_depends(AddAvatarToUserImpl)

    app.dependency_overrides[RegisterUser] = RegisterUserImpl
    app.dependency_overrides[ActivateUser] = ActivateUserImpl
    app.dependency_overrides[ResendActivationEmail] = ResendActivationEmailImpl
    app.dependency_overrides[AddAvatarToUser] = AddAvatarToUserImpl
