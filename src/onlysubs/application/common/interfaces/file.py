import abc

from onlysubs.domain.models.file import File


class FileStorageLoader(abc.ABC):
    @abc.abstractmethod
    def load_file(self, file: File) -> str:
        raise NotImplementedError
