from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from onlysubs.domain.models.user import UserId

UserAvatarId = NewType("UserAvatarId", int)


@dataclass
class UserAvatar:
    id: UserAvatarId | None
    created_at: datetime
    url: str
    user_id: UserId
