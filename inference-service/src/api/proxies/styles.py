from typing import Any

from fastapi import APIRouter, BackgroundTasks, File, Form, UploadFile
from src.api.handlers.styles_list import styles_list_handler
from src.api.handlers.transfer_style import transfer_style_handler

styles_router = APIRouter()


@styles_router.get("/")
def get_styles():
    return styles_list_handler.handle()


@styles_router.post("/transform")
def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
):
    return transfer_style_handler.handle(file, style, background_tasks)
