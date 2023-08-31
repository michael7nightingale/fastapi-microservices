from pydantic import BaseModel, Field
from datetime import datetime


class AddressCreate(BaseModel):
    city: str
    street: str
    number: str


class OrderCreate(BaseModel):
    address: AddressCreate
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


class Basket(BaseModel):
    user: str
    current: bool


class BasketGoodCreate(BaseModel):
    good: str
    amount: int


class BasketGoodUpdate(BaseModel):
    amount: int | None = None


class BasketGood(BaseModel):
    id: str
    basket: str
    amount: str
    good: str


class UserModel(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False
    is_staff: bool = False
