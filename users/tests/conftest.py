import pytest
import pytest_asyncio
import asyncio
from httpx import AsyncClient

from main import create_app
from src.config import get_test_settings
from src.db.events import create_pool, create_engine, Base
from src.db.services import UserService
from src.routes import router


@pytest.fixture
async def app():
    app_ = create_app(get_test_settings())
    engine = await create_engine(get_test_settings().db_url)
    pool = await create_pool(engine)
    app_.state.pool = pool
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await create_users_test_data(pool)

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


user1_data = {
    "email": "user@gmail.com",
    "password": "password",
    "first_name": "aopsdkasd",
    "last_name": "oa0skndnasm"
}


@pytest_asyncio.fixture
def user1():
    return user1_data


async def create_users_test_data(pool):
    async with pool() as session:
        user_service = UserService(session)
        await user_service.create(**user1_data)


@pytest_asyncio.fixture
async def authorized_client(client: AsyncClient, user1: dict):
    resp = await client.post(
        url=router.url_path_for("token"),
        json=user1_data
    )
    resp_data = resp.json()
    access_token = resp_data['access-token']
    client.headers['Authorization'] = f"Token {access_token}"
    return client
