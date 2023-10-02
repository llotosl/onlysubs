import abc
from onlysubs.application.common.interfaces.avatar import UserAvatarSaver
from onlysubs.application.common.interfaces.file import FileSaver, FileStorageLoader
from onlysubs.application.common.interfaces.user import UserByIdChecker


class FileRepository(FileSaver, abc.ABC):
    pass


class FileStorageGateway(FileStorageLoader, abc.ABC):
    pass


class UserRepository(UserByIdChecker, abc.ABC):
    pass


class UserAvatarRepository(UserAvatarSaver, abc.ABC):
    pass
