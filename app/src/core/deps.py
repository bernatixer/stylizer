from typing import Any, Generator
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.exceptions.insufficient_tokens_exception import InsufficientTokensException
from src.core.logger import LOG
from src.schemas.user import User
from src.core.auth import decode_token, security_scheme
from src.repositories.users import users_repository
from db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(security_scheme)):
    user_id = decode_token(token)
    
    user = users_repository.get(db=db, id=user_id)
    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid token",
        )
    
    return User(id=user.id, email=user.email, tokens=user.tokens)


def authenticate_request(_: User = Depends(get_current_user)) -> None:
    return


class CallCost:
    def __init__(self, token_cost: int) -> None:
        self.token_cost = token_cost

    def __call__(self, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> Any:
        try:
            if current_user.tokens - self.token_cost < 0:
                raise InsufficientTokensException()
            users_repository.substract_user_tokens(db=db, user_id=current_user.id, tokens=self.token_cost)
            yield
        except InsufficientTokensException as e:
            raise e
        except Exception as e:
            users_repository.add_user_tokens(db=db, user_id=current_user.id, tokens=self.token_cost)
            raise e
