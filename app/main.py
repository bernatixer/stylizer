import logging
from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from styles.styles import Styles

from routes.router import api_router

# logging.basicConfig(level=logging.INFO)

from pythonjsonlogger import jsonlogger

logHandler = logging.FileHandler(filename='/var/log/stylizer.log')
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

app = FastAPI()
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.info("Starting Stylizer app")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("Stopping Stylizer app")
