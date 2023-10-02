from dataclasses import dataclass, field
from datetime import datetime
from typing import NewType

from src.domain.models.file import File, FileId
from src.domain.models.user import UserId

UserAvatarId = NewType("UserAvatarId", int)


@dataclass
class UserAvatar:
    id: UserAvatarId = field(init=False)
    file: File = field(init=False)
    file_id: FileId
    user_id: UserId
    created_at: datetime
