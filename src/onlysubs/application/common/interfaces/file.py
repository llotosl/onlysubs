import abc

from onlysubs.application.common.dto.file import LoadFileDTO
from onlysubs.domain.models.file import File
from onlysubs.domain.models.url import URL


class FileStorageLoader(abc.ABC):
    @abc.abstractmethod
    async def load_file(self, data: LoadFileDTO) -> URL:
        raise NotImplementedError


class FileSaver(abc.ABC):
    @abc.abstractmethod
    async def save_file(self, file: File) -> None:
        raise NotImplementedError
