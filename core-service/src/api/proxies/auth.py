from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.api.proxies.models.auth_user_signup_request import UserSignupRequest
from src.api.proxies.models.auth_user_login_request import UserLoginRequest
from src.core.deps import get_db
from src.repositories.users import users_repository
from src.core.auth_service import auth_service
from src.core.deps import get_current_user
from src.schemas.user import User

auth_router = APIRouter()


# TODO - Add throttling
@auth_router.post("/signup")
def signup(*, db: Session = Depends(get_db), user_data: UserSignupRequest):
    user = users_repository.get_user_by_email(db=db, email=user_data.email)
    
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists",
        )
    
    return users_repository.create(db=db, obj_in=User(email=user_data.email, tokens=100))


@auth_router.post("/login")
def login(*, db: Session = Depends(get_db), user_data: UserLoginRequest):
    user = users_repository.get_user_by_email(db=db, email=user_data.email)
    
    return {
        "access_token": auth_service.create_access_token(sub=user.id),
        "token_type": "bearer",
    }


@auth_router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return current_user


@auth_router.get("/users")
def users(*, db: Session = Depends(get_db)):
    return users_repository.get_multi(db=db)
