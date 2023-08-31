from sqlalchemy import String, Column, ForeignKey

from .events import Base
from ..base import SQLAlchemyModel


class Country(SQLAlchemyModel, Base):
    __tablename__ = "countries"

    name = Column(String(125))


class City(SQLAlchemyModel, Base):
    __tablename__ = "cities"

    name = Column(String(125))
    country = Column(String(200), ForeignKey("countries.id"))


class Address(SQLAlchemyModel, Base):
    __tablename__ = "addresses"

    city = Column(String(200), ForeignKey("cities.id"))
    street = Column(String(100))
    number = Column(String(10))
