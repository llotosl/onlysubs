from datetime import UTC, datetime

import jwt

from onlysubs.application.common.interfaces.token import ActivationCryptor
from onlysubs.domain.dto.user_activation import (
    UserActivation,
    UserActivationToken,
)


class JWTActivationCryptor(ActivationCryptor):
    def __init__(self, secret_key: str, algorithm_type: str) -> None:
        self.secret_key = secret_key
        self.algorithm_type = algorithm_type

    def encrypt(self, activation: UserActivation) -> UserActivationToken:
        token = jwt.encode(
            {
                "user_id": activation.user_id,
                "active_till": activation.active_till.timestamp(),
            },
            self.secret_key,
            algorithm=self.algorithm_type,
        )

        return UserActivationToken(token)

    def decrypt(self, token: UserActivationToken) -> UserActivation:
        payload_data = jwt.decode(
            token,
            self.secret_key,
            algorithms=[self.algorithm_type],
        )
        payload = UserActivation(
            user_id=payload_data["user_id"],
            active_till=datetime.fromtimestamp(
                payload_data["active_till"],
                tz=UTC,
            ),
        )
        return payload
