import logging

from onlysubs.application.common.dto.emails import SendUserActivationEmailDTO
from onlysubs.application.common.interfaces.emails import (
    UserActivationEmailSender, UserConfirmationEmailSender)

logger = logging.getLogger(__name__)


class StdoutEmailSender(UserConfirmationEmailSender, UserActivationEmailSender):
    async def send_user_activation_email(
        self,
        data: SendUserActivationEmailDTO,
    ) -> None:
        activation_email = (
            f"Send activation email to {data.user_email}:\n"
            + "Hey, dear user! Please, go to this url to activate your account:\n"
            + f"{data.activation_url}"
        )
        print(activation_email)

    async def send_user_confirmation_email(self, user_email: str) -> None:
        confirmation_email = (
            f"Send confirmation email to {user_email}:\n"
            + "Hey, dear user! Thank you for using our service."
        )
        print(confirmation_email)
