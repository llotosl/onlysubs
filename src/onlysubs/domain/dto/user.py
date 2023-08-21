from dataclasses import dataclass

from onlysubs.domain.models.user import Username


@dataclass(frozen=True)
class CreateUserDTO:
    username: Username
    first_name: str
    last_name: str
    password: str
