import abc

from src.application.common.dto.file import LoadFileDTO
from src.domain.models.file import File
from src.domain.models.url import URL


class FileStorageLoader(abc.ABC):
    @abc.abstractmethod
    async def load_file(self, data: LoadFileDTO) -> URL:
        raise NotImplementedError


class FileSaver(abc.ABC):
    @abc.abstractmethod
    async def save_file(self, file: File) -> None:
        raise NotImplementedError
