import datetime

from pydantic import BaseModel, Field


class Company(BaseModel):
    id: str
    title: str
    description: str
    country: str


class Category(BaseModel):
    id: str
    title: str


class Subcategory(BaseModel):
    id: str
    title: str
    category: str


class SubcategoryFull(Subcategory):
    id: str
    title: str
    category: Category


class CategoryFull(Category):
    subcategories: list[Subcategory]


class DescriptionTagCreate(BaseModel):
    good: str
    tag: str
    text: str


class GoodCreate(BaseModel):
    title: str
    description: str
    subcategory: str
    price: int
    discount: int
    # company: str
    description_tags: list[DescriptionTagCreate] = Field(default_factory=list)


class GoodUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    subcategory: str | None = None
    price: int | None = None
    discount: int | None = None


class Good(BaseModel):
    id: str
    title: str
    description: str
    subcategory: str
    price: int
    discount: int


class GoodFull(Good):
    subcategory: Subcategory
    category: Category


class DescriptionTagUpdate(BaseModel):
    good: str | None = None
    tag: str | None = None
    text: str | None = None


class DescriptionTag(BaseModel):
    id: str
    good: str
    tag: str
    text: str


class BasketGoodCreate(BaseModel):
    amount: int = Field(default=1)
    good: str


class BasketGood(BasketGoodCreate):
    id: str


class BasketGoodUpdate(BaseModel):
    amount: int


class BasketGoodFull(BasketGood):
    good: Good


class Basket(BaseModel):
    id: str
    user: str


class BasketFull(BaseModel):
    id: str
    user: str
    basket_goods: list[BasketGood] = Field(default_factory=list)


class OrderCreate(BaseModel):
    user: str
    address: str


class Order(OrderCreate):
    basket: str
    is_paid: str
    time_created: datetime.datetime
    time_finished: datetime.datetime


class Address(BaseModel):
    city: str
    street: str
    number: str


class OrderFull(Order):
    basket: Basket
    address: Address


class UserModel(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False
    is_staff: bool = False
