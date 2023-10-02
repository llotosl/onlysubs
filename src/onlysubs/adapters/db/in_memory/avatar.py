from onlysubs.application.common.interfaces.avatar import UserAvatarSaver
from onlysubs.domain.models.avatar import UserAvatar, UserAvatarId

avatar_data: dict[int, UserAvatar] = {}
avatar_id = 0


class InMemoryAvatarRepository(UserAvatarSaver):
    async def save_avatar(self, avatar: UserAvatar) -> None:
        global avatar_data
        global avatar_id
        avatar_id += 1

        avatar_data[avatar_id] = avatar
        avatar.id = UserAvatarId(avatar_id)
