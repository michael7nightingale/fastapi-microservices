from sqlalchemy.ext.asyncio import AsyncSession
from passlib.hash import sha256_crypt

from .models import Order
from .repositories import AsyncSQLAlchemyRepository


class AsyncSQLAlchemyService:
    """
    Service class to serve sqlalchemy object by async engine and sessions.
    """
    repository_class = AsyncSQLAlchemyRepository    # async repository, of course
    model = None   # inherits must have cls attribute ot their models

    def __init__(self, session: AsyncSession):
        self._repository = self.repository_class(session=session, model=self.model)

    @property
    def repository(self):
        return self._repository

    async def get(self, *args, **kwargs):
        """Get object."""
        return await self.repository.get(*args, **kwargs)

    async def delete(self, id_: str):
        """Delete object."""
        return await self.repository.delete(id_)

    async def update(self, id_: str, **kwargs):
        """Update object."""
        return await self.repository.update(id_, **kwargs)

    async def all(self):
        """Get all objects."""
        return await self.repository.all()

    async def filter(self, **kwargs):
        """Filter objects."""
        return await self.repository.filter(**kwargs)

    async def create(self, **kwargs):
        """Create object."""
        return await self.repository.create(**kwargs)


class OrderService(AsyncSQLAlchemyService):
    model = Order
