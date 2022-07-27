import logging
from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile
from fastapi.staticfiles import StaticFiles
from styles.styles import Styles

from routes.router import api_router


logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
