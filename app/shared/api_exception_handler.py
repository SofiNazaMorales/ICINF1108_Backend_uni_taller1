from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from app.shared.api_response import ApiResponse


async def api_exception_handler(
    request: Request,
    exc: HTTPException,
) -> JSONResponse:
    response = ApiResponse(
        success=False,
        message=str(exc.detail),
        data=None,
        statusCode=exc.status_code,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=response.model_dump(),
    )