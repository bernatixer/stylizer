from fastapi import APIRouter
from handlers.index import IndexHandler

import logging


router = APIRouter()
logger = logging.getLogger()

@router.get("/")
def index():
    logger.info("Hello world log")
    index_handler = IndexHandler()
    return index_handler.handle()
