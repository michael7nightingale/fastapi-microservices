from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    GATEWAY_URL: str

    ALGORITHM: str
    SECRET_KEY: str
    EXPIRE_MINUTES: int

    @property
    def db_url(self):
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}".format(
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            name=self.DB_NAME
        )

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
