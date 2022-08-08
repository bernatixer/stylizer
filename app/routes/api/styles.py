from typing import Any

from core.deps import get_db
from fastapi import APIRouter, BackgroundTasks, Depends, File, Form, UploadFile
from api.handlers.styles_list import styles_list_handler
from api.handlers.transfer_style import transfer_style_handler
from api.handlers.transfered_styles import transfered_styles_handler
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
def get_styles(db: Session = Depends(get_db)) -> Any:
    return styles_list_handler.handle(db)


@router.get("/transform")
def stylize_image(db: Session = Depends(get_db)):
    return transfered_styles_handler.handle(db)


@router.post("/transform")
def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
    db: Session = Depends(get_db),
):
    return transfer_style_handler.handle(file, style, background_tasks, db)
