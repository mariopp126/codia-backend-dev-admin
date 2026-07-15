from pathlib import Path
from typing import Optional

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration settings.

    Values are loaded from the .env file in the project root.
    Missing variables fall back to the defaults defined here.
    """

    # Application
    app_name: str = "Codia Management API"
    debug: bool = False

    # Database — shared PostgreSQL instance with Reporting API.
    postgres_host: str = "dev-postgres"
    postgres_port: int = 5432
    postgres_db: str = "app_db"
    postgres_user: str = "app_user"
    postgres_password: str = "app_password"

    database_url: str = ""

    # Schemas the Management API may read from.
    # The Management API owns the "management" schema and has read-only
    # access to all Reporting API schemas.
    db_schemas: list[str] = ["identity", "reporting", "media", "inspector", "management"]

    # JWT — must match Reporting API for token validation.
    jwt_secret_key: str = "your-super-secret-key-change-this-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:8080", "http://localhost:5173"]
    cors_origin_regex: Optional[str] = r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$"
    cors_credentials: bool = True
    cors_methods: list[str] = ["*"]
    cors_headers: list[str] = ["*"]

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    @model_validator(mode="after")
    def _build_database_url(self) -> "Settings":
        """Compute DATABASE_URL from components if not explicitly set."""
        if not self.database_url:
            self.database_url = (
                f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
                f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
            )
        elif self.database_url.startswith("postgresql://"):
            self.database_url = self.database_url.replace(
                "postgresql://", "postgresql+psycopg2://", 1
            )
        return self


settings = Settings()
