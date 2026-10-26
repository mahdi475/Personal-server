from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """App settings, read from environment variables or the .env file."""

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")

    database_url: str


settings = Settings()
