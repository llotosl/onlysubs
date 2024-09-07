import abc

from onlysubs.domain.dto.user_activation import (
    UserActivation,
    UserActivationToken,
)


class ActivationCryptor(abc.ABC):
    @abc.abstractmethod
    def encrypt(self, activation: UserActivation) -> UserActivationToken:
        raise NotImplementedError

    @abc.abstractmethod
    def decrypt(self, token: UserActivationToken) -> UserActivation:
        raise NotImplementedError
