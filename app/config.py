from pydantic import BaseSettings


class Settings(BaseSettings):
    domain: str = "http://127.0.0.1:8000"
    static_folder: str = "static"

    class Config:
        env_file = ".env"


settings = Settings()
