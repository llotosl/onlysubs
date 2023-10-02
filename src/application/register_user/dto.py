from dataclasses import dataclass

from src.domain.models.email import Email
from src.domain.models.user import Username


@dataclass(frozen=True)
class RegisterUserDTO:
    email: Email
    first_name: str
    last_name: str
    username: Username
    password: str
