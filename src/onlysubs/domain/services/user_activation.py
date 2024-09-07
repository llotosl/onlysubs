from datetime import UTC, datetime, timedelta

from onlysubs.domain.dto.user_activation import UserActivation
from onlysubs.domain.exceptions.user_activation import (
    UserActivationTokenExpiredError,
)
from onlysubs.domain.models.user import User


class UserActivationService:
    def __init__(
        self,
        activity_delta: timedelta,
    ) -> None:
        self.activity_delta = activity_delta

    def activate_user(self, user: User) -> None:
        user.is_active = True

    def create_user_activation(self, user: User) -> UserActivation:
        return UserActivation(
            user_id=user.id,
            active_till=datetime.now(tz=UTC) + self.activity_delta,
        )

    def validate_user_activation(
        self,
        user_activation: UserActivation,
    ) -> None:
        if user_activation.active_till < datetime.now(tz=UTC):
            raise UserActivationTokenExpiredError
