import abc
from typing import Protocol


class ReadableFile(Protocol):
    @abc.abstractmethod
    async def read(self) -> bytes:
        raise NotImplementedError
