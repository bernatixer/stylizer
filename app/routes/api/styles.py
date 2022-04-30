from typing import Any

from fastapi import APIRouter, File, Form, BackgroundTasks, UploadFile
from handlers.styles_list import StylesListHandler
from handlers.transfer_style import TransferStyleHandler

router = APIRouter()


@router.get("/")
def get_styles() -> Any:
    styles_list_handler = StylesListHandler()
    return styles_list_handler.handle()


@router.post("/transform")
def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
):
    transfer_style_handler = TransferStyleHandler()
    return transfer_style_handler.handle(file, style, background_tasks)
