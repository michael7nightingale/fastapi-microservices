from sqlalchemy import String, Column, ForeignKey, Boolean, DateTime

from .events import Base
from ..base import SQLAlchemyModel


class Basket(SQLAlchemyModel, Base):
    __tablename__ = "baskets"

    user = Column(String(200), ForeignKey("users.id"), unique=True)


class BasketGood(SQLAlchemyModel, Base):
    __tablename__ = "basketgoods"

    basket = Column(String(200), ForeignKey("baskets.id"))
    good = Column(String(200), ForeignKey("goods.id"))


class Order(SQLAlchemyModel, Base):
    __tablename__ = "orders"

    basket = Column(String(200), ForeignKey("baskets.id"))
    address = Column(String(200), ForeignKey("addresses.id"))
    is_paid = Column(Boolean(), default=False)
    time_created = Column(DateTime(timezone=True))
    time_finished = Column(DateTime(timezone=True), nullable=True)
