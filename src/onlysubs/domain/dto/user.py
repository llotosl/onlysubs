from dataclasses import dataclass

from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import Username


@dataclass(frozen=True)
class CreateUserDTO:
    username: Username
    email: Email
    first_name: str
    last_name: str
    password: str
    is_active: bool
