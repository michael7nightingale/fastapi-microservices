from fastapi import FastAPI
from fastapi_authtools import AuthManager
from tortoise.contrib.fastapi import register_tortoise

from src.config import get_settings
from src.routes import router


app = FastAPI()
app.include_router(router)
app.state.auth_manager = AuthManager(
    app=app,
    algorithm="HS256",
    secret_key="asdpokaldfsa",
    expire_minutes=60*24,
)


@app.on_event("startup")
async def on_startup():
    register_tortoise(
        app=app,
        db_url=get_settings().db_url,
        modules={"models": ['src.models']},
        generate_schemas=True
    )
