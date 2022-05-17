from typing import Any

from fastapi import APIRouter, File, Form, BackgroundTasks, UploadFile, Depends
from sqlalchemy.orm import Session
from handlers.styles_list import styles_list_handler
from handlers.transfer_style import transfer_style_handler
from deps import get_db

router = APIRouter()


@router.get("/")
def get_styles(db: Session = Depends(get_db)) -> Any:
    return styles_list_handler.handle(db)


@router.post("/transform")
def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
):
    return transfer_style_handler.handle(file, style, background_tasks)
