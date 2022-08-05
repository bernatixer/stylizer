import time

from config import settings
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from logger import LOG
from routes.router import api_router

app = FastAPI()
app.include_router(api_router)
app.mount(
    f"/{settings.STATIC_FOLDER}",
    StaticFiles(directory=settings.STATIC_FOLDER),
    name=settings.STATIC_FOLDER,
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
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
