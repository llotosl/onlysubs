import abc

from onlysubs.application.common.dto.emails import SendUserActivationEmailDTO
from onlysubs.application.common.exceptions import (
    UserEmailAlreadyExistsError,
    UsernameAlreadyExistsError,
)
from onlysubs.application.common.interfaces.uow import UoW
from onlysubs.application.common.use_case import UseCase
from onlysubs.application.register_user.dto import RegisterUserDTO
from onlysubs.application.register_user.interfaces import (
    EmailSender,
    UserRepository,
)
from onlysubs.domain.dto.user import CreateUserDTO
from onlysubs.domain.models.user import User
from onlysubs.domain.services.user import UserService
from onlysubs.domain.services.user_activation import UserActivationService


class RegisterUser(UseCase[RegisterUserDTO, User], abc.ABC):
    pass


class RegisterUserImpl(RegisterUser):
    def __init__(
        self,
        user_repo: UserRepository,
        user_service: UserService,
        user_activation_service: UserActivationService,
        email_sender: EmailSender,
        uow: UoW,
    ) -> None:
        self.user_repo = user_repo
        self.user_service = user_service
        self.user_activation_service = user_activation_service
        self.email_sender = email_sender
        self.uow = uow

    async def __call__(self, data: RegisterUserDTO) -> User:
        await self.__check_if_email_available(data)
        await self.__check_if_username_available(data)

        user = await self.__create_user(data)

        await self.__send_activation_email_to_user(user)

        await self.uow.commit()
        return user

    async def __check_if_email_available(self, data: RegisterUserDTO) -> None:
        is_email_not_available = await self.user_repo.is_user_exists_by_email(
            data.email,
        )
        if is_email_not_available:
            raise UserEmailAlreadyExistsError(email=data.email)

    async def __check_if_username_available(
        self,
        data: RegisterUserDTO,
    ) -> None:
        is_username_not_available = (
            await self.user_repo.is_user_exists_by_username(
                data.username,
            )
        )
        if is_username_not_available:
            raise UsernameAlreadyExistsError(username=data.username)

    async def __create_user(self, data: RegisterUserDTO) -> User:
        user = self.user_service.create_user(
            CreateUserDTO(
                username=data.username,
                email=data.email,
                first_name=data.first_name,
                last_name=data.last_name,
                password=data.password,
                is_active=False,
            ),
        )
        await self.user_repo.save_user(user)
        return user

    async def __send_activation_email_to_user(self, user: User) -> None:
        token = self.user_activation_service.create_token_for_user(user)
        await self.email_sender.send_user_activation_email(
            SendUserActivationEmailDTO(
                user_email=user.email,
                activation_url=f"https://front.com/?token={token}",
            ),
        )
