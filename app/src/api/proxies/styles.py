from typing import Any

from fastapi import APIRouter, BackgroundTasks, Depends, File, Form, UploadFile, Request
from src.core.deps import authenticate_request
from src.core.deps import CallCost
from src.core.deps import get_db
from src.api.handlers.styles_list import styles_list_handler
from src.api.handlers.transfer_style import transfer_style_handler
from src.api.handlers.transfered_styles import transfered_styles_handler
from sqlalchemy.orm import Session
from src.core.deps import get_current_user
from src.schemas.user import User

styles_router = APIRouter()


@styles_router.get("/")
def get_styles():
    return styles_list_handler.handle()


@styles_router.get("/transform")
def stylize_image(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return transfered_styles_handler.handle(db, current_user)


@styles_router.post("/transform", dependencies=(Depends(authenticate_request), Depends(CallCost(token_cost=10))))
def stylize_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    style: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return transfer_style_handler.handle(file, style, background_tasks, db, current_user)
