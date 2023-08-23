from pydantic import BaseModel, Field
from datetime import datetime


class OrderCreate(BaseModel):
    user: str
    address: str
    good: str | None = None
    is_paid: bool = False
    time_created: datetime = Field(default_factory=datetime.utcnow)
    time_finished: datetime = Field(default_factory=datetime.utcnow)


class Order(BaseModel):
    id: str
    user: str
    address: str
    good: str | None = None
    is_paid: bool
    time_created: datetime
    time_finished: datetime


class UserModel(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False
    is_staff: bool = False
