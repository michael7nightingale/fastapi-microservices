from tortoise import fields
from tortoise.exceptions import IntegrityError

from passlib.hash import sha256_crypt

from .base import TortoiseModel


class User(TortoiseModel):
    email = fields.CharField(max_length=100, unique=True, index=True)
    password = fields.CharField(max_length=200)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)

    @classmethod
    async def create(cls, **kwargs):
        if "password" in kwargs:
            kwargs.update(password=sha256_crypt.hash(kwargs['password']))
        try:
            return await super().create(**kwargs)
        except IntegrityError:
            return None

    @classmethod
    async def login(cls, email: str, password: str):
        user = await cls.get_or_none(email=email)
        if user is not None:
            if sha256_crypt.verify(password, user.password):
                return user

    class Meta:
        table = "users"
