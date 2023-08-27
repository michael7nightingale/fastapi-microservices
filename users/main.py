from fastapi import FastAPI
from fastapi_authtools import AuthManager

from src.config import get_settings
from src.routes import router
from src.db.events import create_engine, create_pool
from src.datasructures import UserModel


def create_app(settings=get_settings()):
    app = FastAPI()
    app.include_router(router)
    app.state.auth_manager = AuthManager(
        app=app,
        algorithm=settings.ALGORITHM,
        secret_key=settings.SECRET_KEY,
        expire_minutes=settings.EXPIRE_MINUTES,
        user_model=UserModel
    )

    @app.on_event("startup")
    async def on_startup():
        """Startup handler."""
        engine = await create_engine(db_url=settings.db_url)
        pool = await create_pool(engine)
        app.state.pool = pool
    return app
