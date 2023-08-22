from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USER_SERVICE_URL: str
    LOCATIONS_SERVICE_URL: str
    STORES_SERVICE_URL: str

    DB_URL: str

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
