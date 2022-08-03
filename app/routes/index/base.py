from fastapi import APIRouter
from handlers.index import IndexHandler

router = APIRouter()

import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.FileHandler(filename='/var/log/stylizer.log')
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

@router.get("/")
def index():
    logger.info("Hello world log")
    index_handler = IndexHandler()
    return index_handler.handle()
