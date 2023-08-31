from sqlalchemy import select, delete, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


class BaseAlchemyModel:
    pass


class AsyncSQLAlchemyRepository:

    def __init__(self, model, session: AsyncSession):
        self._model = model
        self._session = session

    async def create(self, **kwargs) -> BaseAlchemyModel | None:
        """Create new object in the table"""
        try:
            new_obj = self._model(
                **kwargs
            )
            await self.save(new_obj)
            return new_obj
        except IntegrityError:
            await self._session.rollback()
            return None

    async def get(self, *args, **kwargs) -> BaseAlchemyModel | None:
        """Get object by pk (id) or other."""
        if len(args) == 1:
            kwargs.update(id=args[0])
        elif len(args) > 1:
            raise ValueError("1 id arg expected.")
        expected = (
            getattr(self._model, key) == value for key, value in kwargs.items()
        )
        query = select(self._model).where(*expected)
        return (await self._session.execute(query)).scalar_one_or_none()

    async def filter(self, **kwargs) -> list[BaseAlchemyModel]:
        """Filter all objects by kwargs"""
        query = select(self._model).filter_by(**kwargs)
        return (await self._session.execute(query)).scalars().all()

    async def all(self) -> list[BaseAlchemyModel]:
        """Get all objects from the table"""
        query = select(self._model)
        return (await self._session.execute(query)).scalars().all()

    async def update(self, id_, strict_nullable=False, **kwargs) -> None:
        """Update object by pk (id) with values kwargs"""
        if not strict_nullable:
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
        query = update(self._model).where(self._model.id == id_).values(**kwargs)
        await self._session.execute(query)
        await self.commit()

    async def delete(self, id_) -> None:
        """Delete object by pk (id)"""
        query = delete(self._model).where(self._model.id == id_)
        await self._session.execute(query)
        await self.commit()

    async def commit(self):
        """Comfortably commit changes"""
        await self._session.commit()

    async def add(self, obj):
        """Comfortably add object"""
        self._session.add(obj)

    async def save(self, obj):
        await self.add(obj)
        await self.commit()
