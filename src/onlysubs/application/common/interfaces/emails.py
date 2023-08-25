import abc

from onlysubs.application.common.dto.emails import (
    SendUserActivationEmailDTO,
)


class UserActivationEmailSender(abc.ABC):
    @abc.abstractmethod
    async def send_user_activation_email(
        self,
        data: SendUserActivationEmailDTO,
    ) -> None:
        raise NotImplementedError


class UserConfirmationEmailSender(abc.ABC):
    @abc.abstractmethod
    async def send_user_confirmation_email(self, user_email: str) -> None:
        raise NotImplementedError
