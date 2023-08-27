from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Order, Basket, BasketGood
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

    async def create_order(self, user_id: str, **kwargs):
        query = select(Basket).where(Basket.user == user_id, Basket.current == True)
        basket = (await self.repository.session.execute(query)).select_one_or_none()
        if basket is None:
            return None
        else:
            return await self.create(backet=basket.id, **kwargs)


class BasketService(AsyncSQLAlchemyService):
    model = Basket


class BasketGoodService(AsyncSQLAlchemyService):
    model = BasketGood
