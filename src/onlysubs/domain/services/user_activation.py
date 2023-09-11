from datetime import UTC, datetime, timedelta

import jwt

from onlysubs.domain.dto.user_activation import UserActivationTokenPayloadDTO
from onlysubs.domain.exceptions.user_activation import UserActivationTokenExpired
from onlysubs.domain.models.user import User
from onlysubs.domain.models.user_activation import UserActivationToken


class UserActivationService:
    def __init__(
        self,
        secret_key: str,
        algorithm_type: str,
        activity_delta: timedelta,
    ) -> None:
        self.secret_key = secret_key
        self.algorithm_type = algorithm_type
        self.activity_delta = activity_delta

    def activate_user(self, user: User) -> None:
        user.is_active = True

    def create_token_for_user(self, user: User) -> UserActivationToken:
        payload = UserActivationTokenPayloadDTO(
            user_id=user.id,
            active_till=datetime.now(tz=UTC) + self.activity_delta,
        )
        token = jwt.encode(
            {
                "user_id": payload.user_id,
                "active_till": payload.active_till.timestamp(),
            },
            self.secret_key,
            algorithm=self.algorithm_type,
        )
        return UserActivationToken(token)

    def get_payload_from_token(
        self,
        token: UserActivationToken,
    ) -> UserActivationTokenPayloadDTO:
        payload_data = jwt.decode(token, self.secret_key)
        payload = UserActivationTokenPayloadDTO(
            user_id=payload_data["user_id"],
            active_till=datetime.fromtimestamp(payload_data["active_till"], tz=UTC),
        )
        self.__raise_if_token_payload_expired(payload)
        return payload

    def __raise_if_token_payload_expired(
        self,
        payload: UserActivationTokenPayloadDTO,
    ) -> None:
        if payload.active_till < datetime.now(tz=UTC):
            raise UserActivationTokenExpired
