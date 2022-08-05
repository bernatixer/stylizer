from fastapi import APIRouter
from handlers.index import IndexHandler


router = APIRouter()

@router.get("/")
def index():
    index_handler = IndexHandler()
    return index_handler.handle()
