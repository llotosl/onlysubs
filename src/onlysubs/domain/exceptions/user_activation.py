from onlysubs.domain.exceptions.common import DomainError


class UserActivationTokenInvalidError(DomainError):
    pass


class UserActivationTokenExpiredError(DomainError):
    pass
