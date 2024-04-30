from dataclasses import dataclass

from onlysubs.domain.models.user_activation import UserActivationToken


@dataclass
class ActivateUserDTO:
    activation_token: UserActivationToken
