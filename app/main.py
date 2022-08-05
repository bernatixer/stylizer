import logging
from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile, Request
from fastapi.staticfiles import StaticFiles
from styles.styles import Styles

from routes.router import api_router


app = FastAPI()
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    LOG.info(response, extras={level: 200})
    return response
