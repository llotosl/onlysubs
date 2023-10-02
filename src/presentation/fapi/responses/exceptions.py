from typing import Generic, TypeVar

from pydantic import BaseModel

TData = TypeVar("TData")


class ErrorResult(BaseModel, Generic[TData]):
    message: str
    data: TData
