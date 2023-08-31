from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine
from sqlalchemy.orm import declarative_base


Base = declarative_base()


async def create_engine(db_url: str):
    return create_async_engine(db_url)


async def create_pool(engine: AsyncEngine) -> async_sessionmaker:
    return async_sessionmaker(bind=engine, expire_on_commit=False)
