from onlysubs.domain.exceptions.common import DomainError


class UserActivationTokenInvalid(DomainError):
    pass


class UserActivationTokenExpired(DomainError):
    pass
