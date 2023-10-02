import abc

from onlysubs.application.common.dto.emails import SendUserActivationEmailDTO
from onlysubs.application.common.exceptions import UserEmailNotFoundError
from onlysubs.application.common.use_case import UseCase
from onlysubs.application.resend_activation_email.dto import (
    ResendActivationEmailDTO,
)
from onlysubs.application.resend_activation_email.interfaces import (
    EmailSender,
    UserRepository,
)
from onlysubs.domain.services.user_activation import UserActivationService


class ResendActivationEmail(UseCase[ResendActivationEmailDTO, None], abc.ABC):
    pass


class ResendActivationEmailImpl(ResendActivationEmail):
    def __init__(
        self,
        user_repository: UserRepository,
        email_sender: EmailSender,
        user_activation_service: UserActivationService,
    ) -> None:
        self.user_repo = user_repository
        self.email_sender = email_sender
        self.user_activation_service = user_activation_service

    async def __call__(self, data: ResendActivationEmailDTO) -> None:
        user = await self.user_repo.get_user_by_email(data.user_email)
        if user is None:
            raise UserEmailNotFoundError(email=data.user_email)

        token = self.user_activation_service.create_token_for_user(user)

        await self.email_sender.send_user_activation_email(
            SendUserActivationEmailDTO(
                user_email=user.email,
                activation_url=f"https://front.com/?token={token}",
            ),
        )
