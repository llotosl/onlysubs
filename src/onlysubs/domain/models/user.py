from dataclasses import dataclass
from typing import NewType

UserId = NewType("UserId", int)
Username = NewType("Username", str)
HashedPassword = NewType("HashedPassword", str)


@dataclass
class User:
    id: UserId | None
    username: Username
    first_name: str
    last_name: str
    password: HashedPassword
