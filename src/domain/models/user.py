from dataclasses import dataclass, field
from datetime import datetime
from typing import NewType

from src.domain.models.email import Email

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

    created_at: datetime
    updated_at: datetime
