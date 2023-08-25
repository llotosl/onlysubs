from onlysubs.application.activate_user.dto import ActivateUserDTO
from onlysubs.application.common.use_case import UseCase
from onlysubs.application.activate_user.interfaces import EmailSender, UserRepository
from onlysubs.domain.services.user_activation import UserActivationService


class ActivateUser(UseCase[ActivateUserDTO, None]):
    def __init__(
        self,
        user_repository: UserRepository,
        user_activation_service: UserActivationService,
        email_sender: EmailSender,
    ) -> None:
        self.user_repository = user_repository
        self.user_activation_service = user_activation_service
        self.email_sender = email_sender

    async def __call__(self, data: ActivateUserDTO) -> None:
        token = self.user_activation_service.get_payload_from_token(
            token=data.activation_token,
        )
        user = await self.user_repository.get_user_by_id(token.user_id)
        self.user_activation_service.activate_user(user)
        await self.user_repository.save_user(user)
        await self.email_sender.send_user_confirmation_email(user_email=user.email)
