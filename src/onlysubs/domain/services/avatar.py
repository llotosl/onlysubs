from datetime import UTC, datetime
from onlysubs.domain.dto.avatar import CreateAvatarDTO
from onlysubs.domain.models.avatar import UserAvatar


class UserAvatarService:
    def create_avatar(self, data: CreateAvatarDTO) -> UserAvatar:
        now = datetime.now(tz=UTC)
        return UserAvatar(
            file_id=data.file_id,
            user_id=data.user_id,
            created_at=now,
        )
