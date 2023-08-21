from pydantic import BaseModel, Field
from fastapi_authtools.models import EmailPasswordToken


class UserModel(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str


class UserRegister(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class TokenCreate(EmailPasswordToken):
    pass


class Token(BaseModel):
    access_token: str = Field(alias='access-token')
