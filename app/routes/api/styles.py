from typing import Any

from fastapi import APIRouter, File, Form, BackgroundTasks, UploadFile
from handlers.styles_list import StylesListHandler
from handlers.transfer_style import TransferStyleHandler
from styles.styles import Styles

router = APIRouter()


@router.get("/")
def get_styles() -> Any:
    styles = Styles()
    styles_list_handler = StylesListHandler(styles)
    return styles_list_handler.handle()



@router.post("/transform")
async def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
):
    styles = Styles()
    transfer_style_handler = TransferStyleHandler(styles)
    return transfer_style_handler.handle(file, style, background_tasks)
