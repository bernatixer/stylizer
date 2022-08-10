from fastapi import APIRouter
from src.routes.api import styles
from src.routes.index import base

api_router = APIRouter()
api_router.include_router(base.router, prefix="")
api_router.include_router(styles.router, prefix="/api/styles")
