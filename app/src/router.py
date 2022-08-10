from fastapi import APIRouter
from src.api.proxies.styles import styles_router
from src.api.proxies.index import index_router
from src.api.proxies.auth import auth_router

api_router = APIRouter()
api_router.include_router(index_router, prefix="")
api_router.include_router(styles_router, prefix="/api/styles")
api_router.include_router(auth_router, prefix="/api/auth")
