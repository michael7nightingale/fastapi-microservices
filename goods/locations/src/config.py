from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

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


class TestSettings(BaseSettings):
    DB_NAME: str = "test.sqlite3"

    ALGORITHM: str = "HS256"
    SECRET_KEY: str = "as09dalsdk"
    EXPIRE_MINUTES: int = 60 * 60 * 24

    @property
    def db_url(self):
        return "sqlite+aiosqlite:///{name}".format(name=self.DB_NAME)


def get_settings() -> Settings:
    return Settings()


def get_test_settings() -> TestSettings:
    return TestSettings()
