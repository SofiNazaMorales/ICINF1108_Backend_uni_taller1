from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    status_code: int
    message: str
    data: T | None = None
    errors: list[str] | None = None

    @classmethod
    def ok(cls, data: T, message: str = "OK", status_code: int = 200) -> "ApiResponse[T]":
        return cls(success=True, status_code=status_code, message=message, data=data)

    @classmethod
    def fail(
        cls, message: str, status_code: int = 400, errors: list[str] | None = None
    ) -> "ApiResponse[None]":
        return cls(success=False, status_code=status_code, message=message, errors=errors)
