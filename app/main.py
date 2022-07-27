import logging
from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from styles.styles import Styles
from pythonjsonlogger import jsonlogger

from routes.router import api_router

logger = logging.getLogger()

logHandler = logging.FileHandler(filename='/var/log/stylizer_logs.json')
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

logger.info('Sign up', extra={'referral_code': '52d6ce'})

app = FastAPI()
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
