from pydantic import BaseModel
from onlysubs.domain.models.user_activation import UserActivationToken


class ActivateUserModel(BaseModel):
    activation_token: UserActivationToken
