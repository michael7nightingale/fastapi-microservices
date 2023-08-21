from pydantic import BaseModel


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
