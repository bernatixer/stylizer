from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    DOMAIN: str
    STATIC_FOLDER: str
    ENVIRONMENT: str

    class Config:
        env_file = ".env"

    def isLocal(self):
        return self.ENVIRONMENT == "local"


settings = Settings()
