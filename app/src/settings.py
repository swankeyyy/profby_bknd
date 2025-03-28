from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    
    DB_URL: str = Field(
        default="postgresql+asyncpg://profby:profby@db:5432/profby",
        description="URL для подключения к PostgreSQL."
    )
    DB_ECHO: bool = Field(
        default=True,
        description="Логирование SQL-запросов."
    )

    URL: str = Field(
        default="127.0.0.1:8000",
        description="URL приложения."
    )
    API_PREFIX: str = Field(
        default="/api",
        description="Префикс для API."
    )

    REVIEWS_STORAGE: str = Field(
        default="./images/reviews",
        description="Директория для хранения изображений отзывов."
    )
    PROFESSIONS_STORAGE: str = Field(
        default="./images/professions",
        description="Директория для хранения изображений профессий."
    )
    SECTIONS_STORAGE: str = Field(
        default="./images/sections",
        description="Директория для хранения изображений секций."
    )

    class Config:
        env_file = "./.env"  
        env_file_encoding = "utf-8"  

settings = Settings()