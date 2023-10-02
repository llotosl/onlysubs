from src.application.common.interfaces.uow import UoW


class InMemoryUoW(UoW):
    async def commit(self) -> None:
        return

    async def rollback(self) -> None:
        return

    async def flush(self) -> None:
        return
