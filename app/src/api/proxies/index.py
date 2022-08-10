from fastapi import APIRouter
from src.api.handlers.index import IndexHandler

index_router = APIRouter()


@index_router.get("/")
def index():
    index_handler = IndexHandler()
    return index_handler.handle()
