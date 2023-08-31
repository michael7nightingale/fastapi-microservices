from sqlalchemy import String, Column, Boolean

from .events import Base
from ..base import SQLAlchemyModel


class User(SQLAlchemyModel, Base):
    __tablename__ = "users"

    email = Column(String(125), unique=True, index=True)
    password = Column(String(125))
    first_name = Column(String(125))
    last_name = Column(String(125))
    is_staff = Column(Boolean(), default=False)
    is_superuser = Column(Boolean(), default=False)
