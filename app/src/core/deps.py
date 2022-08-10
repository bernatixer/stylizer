from typing import Generator
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.session import SessionLocal
from src.core.auth import decode_token
from src.repositories.users import users_repository


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user_id = decode_token(token)
    
    user = users_repository.get(db=db, id=user_id)
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid token",
        )
    return user
