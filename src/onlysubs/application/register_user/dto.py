from dataclasses import dataclass

from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import Username


@dataclass(frozen=True)
class RegisterUserDTO:
    email: Email
    first_name: str
    last_name: str
    username: Username
    password: str
