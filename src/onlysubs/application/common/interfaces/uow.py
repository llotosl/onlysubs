import abc


class UoW(abc.ABC):
    @abc.abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    async def flush(self) -> None:
        raise NotImplementedError
