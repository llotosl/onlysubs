class ApplicationError(Exception):
    pass


class UserEmailAlreadyUsedError(ApplicationError):
    pass


class UsernameAlreadyUserError(ApplicationError):
    pass


class UserNotFoundError(ApplicationError):
    pass
