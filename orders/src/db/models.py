from sqlalchemy import String, Column, ForeignKey, Boolean, DateTime, Integer, func

from .events import Base
from ..base import SQLAlchemyModel


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
