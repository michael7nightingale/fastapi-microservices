from fastapi import status
from httpx import AsyncClient

from src.routes import router


async def test_register_success(client: AsyncClient):
    body = {
        "email": "password@gmail.com",
        "password": "password",
        "first_name": "Michael",
        "last_name": "Nightingale"
    }
    resp = await client.post(
        url=router.url_path_for("register"),
        json=body
    )
    resp_data = resp.json()
    assert resp.status_code == status.HTTP_200_OK
    assert resp_data['email'] == body['email']
    assert "id" in resp_data


async def test_register_fail_fields(client: AsyncClient):
    body = {
        "email": "password@gmail.com",
        "password": "password",
    }
    resp = await client.post(
        url=router.url_path_for("register"),
        json=body
    )
    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


async def test_register_fail_exists(client: AsyncClient, user1: dict):
    resp = await client.post(
        url=router.url_path_for("register"),
        json=user1
    )
    assert resp.status_code == status.HTTP_400_BAD_REQUEST


async def test_token_success(client: AsyncClient):
    body = {
        "email": "password@gmail.com",
        "password": "password",
        "first_name": "Michael",
        "last_name": "Nightingale"
    }
    resp = await client.post(
        url=router.url_path_for("register"),
        json=body
    )
    token_body = {
        "password": body["password"],
        "email": body["email"],
    }
    resp = await client.post(
        url=router.url_path_for("token"),
        json=token_body
    )
    resp_data = resp.json()
    assert resp.status_code == status.HTTP_200_OK
    assert "access-token" in resp_data
