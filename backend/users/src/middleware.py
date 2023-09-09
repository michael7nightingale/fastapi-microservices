from typing import Awaitable

from fastapi_authtools.exceptions import Responses
from fastapi_authtools.token import decode_jwt_token
from starlette import authentication
from starlette.middleware.authentication import AuthenticationMiddleware as AuthMiddleware
from starlette.requests import HTTPConnection

from src.config import get_settings
from .datasructures import UserModel


class AuthenticationBackend:

    def verify_token(self, token: str, settings=get_settings()):
        scopes = []
        if token is None:
            return scopes, None

        token = token.split()[-1]
        user_data = decode_jwt_token(
            token=token,
            secret_key=settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )
        if user_data is None:
            return scopes, None
        try:
            user = UserModel(**user_data)
            return scopes, user
        except:
            pass
        raise authentication.AuthenticationError(Responses.invalid_credentials)

    def get_token(self, conn: HTTPConnection) -> str:
        token = conn.headers.get("authorization") or conn.headers.get("Authorization")
        return token

    async def authenticate(
            self, conn: HTTPConnection
    ):
        token = self.get_token(conn)
        if token is None:
            raise authentication.AuthenticationError()
        response = self.verify_token(token)
        if isinstance(response, Awaitable):
            response = await response

        scopes, user = response

        return authentication.AuthCredentials(scopes=scopes), user


class AuthenticationMiddleware(AuthMiddleware):

    def __init__(self, app, backend=AuthenticationBackend()):
        super().__init__(app=app, backend=backend)
