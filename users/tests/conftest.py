import pytest
import pytest_asyncio
import asyncio
from httpx import AsyncClient

from main import create_app
from src.config import get_test_settings
from src.db.events import create_pool, create_engine, Base


@pytest.fixture
async def app():
    app_ = create_app(get_test_settings())
    engine = await create_engine(get_test_settings().db_url)
    app_.state.pool = await create_pool(engine)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield app_
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def client(app):
    async with AsyncClient(app=app, base_url="http://localhost:8000/") as client_:
        yield client_
