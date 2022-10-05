from fastapi import APIRouter

index_router = APIRouter()


@index_router.get("/")
def index():
    return {"status": "OK"}
