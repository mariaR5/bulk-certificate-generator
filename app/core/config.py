from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Bulk Certificate Generator"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = False

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

    STORAGE_DIR: Path = BASE_DIR / "storage"
    CERTIFICATES_DIR: Path = STORAGE_DIR / "certificates"
    ARCHIVES_DIR: Path = STORAGE_DIR / "archives"
    DATABASE_URL: str = "sqlite:///./bulk_certs.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    def init_storage(self) -> None:
        self.CERTIFICATES_DIR.mkdir(parents=True, exist_ok=True)
        self.ARCHIVES_DIR.mkdir(parents=True, exist_ok=True)


settings = Settings()
