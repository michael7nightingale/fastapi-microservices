from uuid import uuid4

from sqlalchemy import String, Column, ForeignKey, Integer

from .events import Base
from ..base import SQLAlchemyModel


class Store(SQLAlchemyModel, Base):
    __tablename__ = "countries"

    address = Column(String(200), ForeignKey("addresses.id"))


class Post(SQLAlchemyModel, Base):
    __tablename__ = "posts"

    title = Column(String(200), unique=True, index=True)
    min_salary = Column(Integer())
    max_salary = Column(Integer())


class Employee(SQLAlchemyModel, Base):
    __tablename__ = "employees"

    store = Column(String(200), ForeignKey("stores.id"))
    first_name = Column(String(125))
    last_name = Column(String(125))
    email = Column(String(125), unique=True)
    key = Column(String(200), primary_key=True, default=lambda: str(uuid4()))
    salary = Column(Integer())
    post = Column(String(200), ForeignKey("posts.id"))
