import time

from config import settings
from fastapi import FastAPI, Request
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
    response.headers["X-Process-Time"] = str(process_time)
    LOG.info(response, extra={"level": 200})
    return response
