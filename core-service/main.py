import time

from fastapi import FastAPI, Request, Response
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from src.core.config import settings
from src.core.logger import LOG
from src.router import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(api_router)
app.mount(
    f"/{settings.STATIC_FOLDER}",
    StaticFiles(directory=settings.STATIC_FOLDER),
    name=settings.STATIC_FOLDER,
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Stylizer API docs",
        version="0.0.1",
        description="This page contains Stylizer API documentation",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "static/logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.middleware("http")
async def add_process_time_header(request: Request, call_next) -> Response:
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(request.client)
    LOG.info(
        "Request in middleware",
        extra={
            "status": response.status_code,
            "duration_ms": process_time*1000,
            "client_ip": request.client.host
        }
    )
    return response
