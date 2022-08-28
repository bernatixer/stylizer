from typing import Any

from fastapi import APIRouter, BackgroundTasks, Depends, File, Form, UploadFile, Request
from src.core.deps import authenticate_request
from src.core.deps import CallCost
from src.core.deps import get_db
from src.api.handlers.styles_list import styles_list_handler
from src.api.handlers.transfer_style import transfer_style_handler
from src.api.handlers.transfered_styles import transfered_styles_handler
from sqlalchemy.orm import Session

styles_router = APIRouter()


@styles_router.get("/", dependencies=(Depends(authenticate_request), Depends(CallCost(token_cost=10))))
def get_styles():
    return styles_list_handler.handle()


@styles_router.get("/transform")
def stylize_image(db: Session = Depends(get_db)):
    return transfered_styles_handler.handle(db)


@styles_router.post("/transform")
def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
    db: Session = Depends(get_db),
):
    return transfer_style_handler.handle(file, style, background_tasks, db)
