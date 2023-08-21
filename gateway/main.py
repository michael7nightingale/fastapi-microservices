from fastapi import Request

from core import GateWay
from config import Settings
from datastructures.users import UserRegister, Token, TokenCreate

app = GateWay()


@app.post(
    path="/register",
    service_base_url=Settings().USER_SERVICE_URL,
    response_model=UserRegister,
    body_key="user_data"
)
async def register(request: Request, user_data: UserRegister):
    pass


@app.post(
    path="/token",
    service_base_url=Settings().USER_SERVICE_URL,
    response_model=TokenCreate,
    body_key="token_data"
)
async def register(request: Request, token_data: Token):
    pass
