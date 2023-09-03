from sqlalchemy import select, delete, update, join
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession

from typing import TypeVar, Type

from .models import Company, Category, Subcategory, Good, DescriptionTag


BaseAlchemyModel = TypeVar("BaseAlchemyModel", bound=DeclarativeBase)


class AsyncSQLAlchemyRepository:
    _model: Type[BaseAlchemyModel]

    def __init__(self, session: AsyncSession):
        self._session = session

    @property
    def model(self):
        return self._model

    @property
    def session(self):
        return self._session

    async def create(self, **kwargs) -> BaseAlchemyModel | None:
        """Create new object in the table"""
        try:
            new_obj = self.model(**kwargs)
            await self.save(new_obj)
            return new_obj
        except IntegrityError:
            await self.session.rollback()
            return None

    async def get(self, *args, **kwargs) -> BaseAlchemyModel | None:
        """Get object by pk (id) or other."""
        if len(args) == 1:
            kwargs.update(id=args[0])
        elif len(args) > 1:
            raise ValueError("1 id arg expected.")
        expected = (
            getattr(self.model, key) == value for key, value in kwargs.items()
        )
        query = select(self.model).where(*expected)
        return (await self.session.execute(query)).scalar_one_or_none()

    async def filter(self, **kwargs) -> list[BaseAlchemyModel]:
        """Filter all objects by kwargs"""
        query = select(self.model).filter_by(**kwargs)
        return (await self.session.execute(query)).scalars().all()

    async def all(self) -> list[BaseAlchemyModel]:
        """Get all objects from the table"""
        query = select(self.model)
        return (await self.session.execute(query)).scalars().all()

    async def update(self, id_, **kwargs) -> None:
        """Update object by pk (id) with values kwargs"""
        query = update(self.model).where(self.model.id == id_).values(**kwargs)
        await self.session.execute(query)
        await self.commit()

    async def delete(self, id_) -> None:
        """Delete object by pk (id)"""
        query = delete(self.model).where(self.model.id == id_)
        await self.session.execute(query)
        await self.commit()

    async def commit(self):
        """Comfortably commit changes"""
        await self.session.commit()

    async def add(self, obj):
        """Comfortably add object"""
        self.session.add(obj)

    async def save(self, obj):
        await self.add(obj)
        await self.commit()


class CategoryRepository(AsyncSQLAlchemyRepository):
    _model = Category

    async def get_with_subcategories(self, id_):
        query = (
            select(Category, Subcategory)
            .join(Subcategory, Subcategory.category == Category.id)
            .where(Category.id == id_)
        )
        data = (await self.session.execute(query)).all()
        if not data:
            return None
        category = data[0][0]
        return {
            **category.as_dict(),
            "subcategories": [row[1].as_dict() for row in data]
        }


class SubcategoryRepository(AsyncSQLAlchemyRepository):
    _model = Subcategory

    async def get_with_category(self, id_):
        query = (
            select(Subcategory, Category)
            .join(Category, Category.id == Subcategory.category)
            .where(Subcategory.id == id_)
        )
        data = (await self.session.execute(query)).all()
        if not data:
            return None
        data = data[0]
        return {
            **data[0].as_dict(),
            "category": data[1].as_dict()
        }


class CompanyRepository(AsyncSQLAlchemyRepository):
    _model = Company


class GoodRepository(AsyncSQLAlchemyRepository):
    _model = Good

    async def get_goods_with_category_and_subcategory(self):
        query = (
            select(Good, Subcategory, Category)
            .join(Subcategory, Subcategory.id == Good.subcategory)
            .join(Category, Category.id == Subcategory.category)
        )
        return [
            {
                **good.as_dict(),
                "subcategory": subcategory.as_dict(),
                "category": category.as_dict()
            }
            for good, subcategory, category in (await self.session.execute(query)).all()
        ]

    async def get_good_with_category_and_subcategory(self, id_: str):
        query = (
            select(Good, Subcategory, Category)
            .join(Subcategory, Subcategory.id == Good.subcategory)
            .join(Category, Category.id == Subcategory.category)
            .where(Good.id == id_)
        )
        data = (await self.session.execute(query)).all()
        if not data:
            return None
        else:
            data = data[0]
            good_data = data[0].as_dict()
            good_data['subcategory'] = data[1].as_dict()
            good_data['category'] = data[2].as_dict()
            return good_data

    async def get_goods_by_category(self, category_id: str):
        query = (
            select(Good, Subcategory, Category)
            .join(Subcategory, Subcategory.id == Good.subcategory)
            .join(Category, Category.id == Subcategory.category)
            .where(Category.id == category_id)
        )
        return [
            {
                **good.as_dict(),
                "subcategory": subcategory.as_dict(),
                "category": category.as_dict()
            }
            for good, subcategory, category in (await self.session.execute(query)).all()
        ]

    async def get_goods_by_subcategory(self, category_id: str):
        query = (
            select(Good, Subcategory, Category)
            .join(Subcategory, Subcategory.id == Good.subcategory)
            .join(Category, Category.id == Subcategory.category)
            .where(Subcategory.id == category_id)
        )
        return [
            {
                **good.as_dict(),
                "subcategory": subcategory.as_dict(),
                "category": category.as_dict()
            }
            for good, subcategory, category in (await self.session.execute(query)).all()
        ]


class DescriptionTagRepository(AsyncSQLAlchemyRepository):
    _model = DescriptionTag
