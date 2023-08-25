from dataclasses import dataclass, field
from typing import NewType

from onlysubs.domain.models.email import Email

UserId = NewType("UserId", int)
Username = NewType("Username", str)
HashedPassword = NewType("HashedPassword", str)


@dataclass
class User:
    id: UserId = field(init=False)
    username: Username
    email: Email
    first_name: str
    last_name: str
    password: HashedPassword
    is_active: bool
