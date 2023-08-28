import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette import status
from starlette.requests import Request

from onlysubs.application.common.exceptions import (
    ApplicationError, UserEmailAlreadyExistsError, UserEmailNotFoundError,
    UserIdNotFoundError, UsernameAlreadyExistsError)
from onlysubs.presentation.fapi.responses.exceptions import ErrorResult

logger = logging.getLogger(__name__)


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        UserEmailAlreadyExistsError,
        user_email_already_exists_error_handler,
    )
    app.add_exception_handler(
        UsernameAlreadyExistsError,
        username_already_exists_error_handler,
    )
    app.add_exception_handler(
        UserIdNotFoundError,
        user_id_not_found_error_handler,
    )
    app.add_exception_handler(
        UserEmailNotFoundError,
        user_email_not_found_error_handler,
    )


async def user_email_already_exists_error_handler(
    request: Request,
    err: UserEmailNotFoundError,
) -> JSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)


async def username_already_exists_error_handler(
    request: Request,
    err: UserEmailNotFoundError,
) -> JSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)


async def user_id_not_found_error_handler(
    request: Request,
    err: UserEmailNotFoundError,
) -> JSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_404_NOT_FOUND)


async def user_email_not_found_error_handler(
    request: Request,
    err: UserEmailNotFoundError,
) -> JSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_404_NOT_FOUND)


async def handle_error(
    request: Request,
    err: ApplicationError,
    status_code: int,
) -> JSONResponse:
    logger.error("Handle error", exc_info=err, extra={"error": err})
    return JSONResponse(
        ErrorResult(message=err.message, data=err).dict(),
        status_code=status_code,
    )
