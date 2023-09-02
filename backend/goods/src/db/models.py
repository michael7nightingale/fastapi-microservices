from sqlalchemy import String, Column, ForeignKey, Text, Integer

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
    # company = Column(String(200), ForeignKey("companies.id"))
    description = Column(Text())
    subcategory = Column(String(200), ForeignKey("subcategories.id"))
    price = Column(Integer())
    discount = Column(Integer())


class DescriptionTag(SQLAlchemyModel, Base):
    __tablename__ = "description_tags"

    good = Column(String(200), ForeignKey("goods.id"))
    tag = Column(String(200))
    text = Column(String(200))
