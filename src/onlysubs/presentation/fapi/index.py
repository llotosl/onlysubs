from fastapi import APIRouter, Request

index_router = APIRouter()


@index_router.get("/")
def healthcheck(
    request: Request,
) -> dict:
    return {"status": "ok"}
