import abc

from onlysubs.domain.models.avatar import UserAvatar


class UserAvatarSaver(abc.ABC):
    @abc.abstractmethod
    async def save_avatar(self, avatar: UserAvatar) -> None:
        raise NotImplementedError
