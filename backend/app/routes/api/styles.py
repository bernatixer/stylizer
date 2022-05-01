from typing import Any

from fastapi import APIRouter, File, Form, BackgroundTasks, UploadFile
from handlers.styles_list import styles_list_handler
from handlers.transfer_style import transfer_style_handler

router = APIRouter()


@router.get("/")
def get_styles() -> Any:
    return styles_list_handler.handle()


@router.post("/transform")
def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
):
    return transfer_style_handler.handle(file, style, background_tasks)
