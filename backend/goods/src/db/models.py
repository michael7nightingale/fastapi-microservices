from sqlalchemy import String, Column, ForeignKey, Text, Integer, func, DateTime, Boolean

from .events import Base
from ..base import SQLAlchemyModel


class Company(SQLAlchemyModel, Base):
    __tablename__ = "companies"

    title = Column(String(200), unique=True, index=True)
    description = Column(Text())
    country = Column(String(200), ForeignKey("countries.id"))


class Category(SQLAlchemyModel, Base):
    __tablename__ = "categories"

    title = Column(String(200), index=True, unique=True)


class Subcategory(SQLAlchemyModel, Base):
    __tablename__ = "subcategories"

    title = Column(String(200), index=True, unique=True)
    category = Column(String(200), ForeignKey("categories.id"))


class Good(SQLAlchemyModel, Base):
    __tablename__ = "goods"

    title = Column(String(200), index=True)
    company = Column(String(200), ForeignKey("companies.id"))
    description = Column(Text())
    subcategory = Column(String(200), ForeignKey("subcategories.id"))
    price = Column(Integer())
    discount = Column(Integer())


class DescriptionTag(SQLAlchemyModel, Base):
    __tablename__ = "description_tags"

    good = Column(String(200), ForeignKey("goods.id"))
    tag = Column(String(200))
    text = Column(String(200))


class User(SQLAlchemyModel, Base):
    __tablename__ = "users"

    email = Column(String(125), unique=True, index=True)
    password = Column(String(125))
    first_name = Column(String(125))
    last_name = Column(String(125))
    is_staff = Column(Boolean(), default=False)
    is_superuser = Column(Boolean(), default=False)



class Basket(SQLAlchemyModel, Base):
    __tablename__ = "baskets"

    user = Column(String(200), ForeignKey("users.id"), unique=True)
    current = Column(Boolean(), default=True)


class BasketGood(SQLAlchemyModel, Base):
    __tablename__ = "basketgoods"

    basket = Column(String(200), ForeignKey("baskets.id"))
    amount = Column(Integer())
    good = Column(String(200), ForeignKey("goods.id"))


class Order(SQLAlchemyModel, Base):
    __tablename__ = "orders"

    user = Column(String(200), ForeignKey("users.id"), unique=True)
    basket = Column(String(200), ForeignKey("baskets.id"))
    address = Column(String(200), ForeignKey("addresses.id"))
    is_paid = Column(Boolean(), default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_finished = Column(DateTime(timezone=True), nullable=True)
