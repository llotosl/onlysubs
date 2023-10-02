import abc

from src.application.common.interfaces.avatar import UserAvatarSaver
from src.application.common.interfaces.file import FileSaver, FileStorageLoader
from src.application.common.interfaces.user import UserByIdChecker


class FileRepository(FileSaver, abc.ABC):
    pass


class FileStorageGateway(FileStorageLoader, abc.ABC):
    pass


class UserRepository(UserByIdChecker, abc.ABC):
    pass


class UserAvatarRepository(UserAvatarSaver, abc.ABC):
    pass
