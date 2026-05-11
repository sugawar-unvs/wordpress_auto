from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "Universe Club Auto Blog Poster"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # Security
    API_KEY: str = ""

    # WordPress
    WP_URL: str = ""
    WP_USERNAME: str = ""
    WP_APP_PASSWORD: str = ""

    # AI
    ANTHROPIC_API_KEY: str = ""
    LITELLM_MODEL: str = "claude-sonnet-4-20250514"

    # Redis / Celery
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    # Upload
    UPLOAD_DIR: str = "/tmp/uploads"
    MAX_UPLOAD_SIZE_MB: int = 10

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
