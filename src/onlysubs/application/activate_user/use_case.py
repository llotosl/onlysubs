import abc

from onlysubs.application.activate_user.dto import ActivateUserDTO
from onlysubs.application.activate_user.interfaces import (
    EmailSender,
    UserRepository,
)
from onlysubs.application.common.exceptions import UserIdNotFoundError
from onlysubs.application.common.interfaces.token import ActivationCryptor
from onlysubs.application.common.interfaces.uow import UoW
from onlysubs.application.common.use_case import UseCase
from onlysubs.domain.services.user_activation import UserActivationService


class ActivateUser(UseCase[ActivateUserDTO, None], abc.ABC):
    pass


class ActivateUserImpl(ActivateUser):
    def __init__(
        self,
        user_repository: UserRepository,
        user_activation_service: UserActivationService,
        email_sender: EmailSender,
        uow: UoW,
        cryptor: ActivationCryptor,
    ) -> None:
        self.user_repository = user_repository
        self.user_activation_service = user_activation_service
        self.email_sender = email_sender
        self.uow = uow
        self.cryptor = cryptor

    async def __call__(self, data: ActivateUserDTO) -> None:
        user_activation = self.cryptor.decrypt(data.activation_token)
        self.user_activation_service.validate_user_activation(user_activation)

        user = await self.user_repository.get_user_by_id(
            user_activation.user_id,
        )
        if user is None:
            raise UserIdNotFoundError(user_activation.user_id)

        self.user_activation_service.activate_user(user)
        await self.user_repository.save_user(user)

        await self.email_sender.send_user_confirmation_email(
            user_email=user.email,
        )

        await self.uow.commit()
