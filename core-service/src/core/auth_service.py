from fastapi import HTTPException, Depends
from datetime import datetime, timedelta
from src.core.config import settings
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer


class AuthService:
    def __init__(self) -> None:
        self.security_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def decode_token(self, token: str):
        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET,
                algorithms=[settings.JWT_ALGORITHM],
                options={"verify_aud": False},
            )
            return payload.get("sub")
        except JWTError:
            raise HTTPException(
                status_code=400,
                detail="Invalid token",
            )


    def create_access_token(self, *, sub: str) -> str:
        return self.create_token(
            token_type="access_token",
            lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
            sub=sub,
        )


    def create_token(
        self,
        token_type: str,
        lifetime: timedelta,
        sub: str,
    ) -> str:
        payload = {}
        expire = datetime.utcnow() + lifetime
        payload["type"] = token_type
        payload["exp"] = expire
        payload["iat"] = datetime.utcnow()
        payload["sub"] = str(sub)

        return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

auth_service = AuthService()
