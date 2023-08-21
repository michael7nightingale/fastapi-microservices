from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    USER_SERVICE_URL: str

    class Config:
        env_file = ".env"
