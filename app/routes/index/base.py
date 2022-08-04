from fastapi import APIRouter
from handlers.index import IndexHandler
from logger import LOG


router = APIRouter()

@router.get("/")
def index():
    LOG.info("Hello world log")
    index_handler = IndexHandler()
    return index_handler.handle()
