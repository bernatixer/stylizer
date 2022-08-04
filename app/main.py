import logging
from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from styles.styles import Styles

from routes.router import api_router
from logger import LOG


app = FastAPI()
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    LOG.info("Starting Stylizer app")


@app.on_event("shutdown")
def shutdown_event():
    LOG.info("Stopping Stylizer app")
