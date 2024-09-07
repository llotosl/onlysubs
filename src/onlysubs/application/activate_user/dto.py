from dataclasses import dataclass

from onlysubs.domain.dto.user_activation import UserActivationToken


@dataclass
class ActivateUserDTO:
    activation_token: UserActivationToken
