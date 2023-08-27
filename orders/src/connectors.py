from typing import Mapping

import aiohttp

from src.config import get_settings


def build_url(path: str, params: dict = {}, base_url=get_settings().GATEWAY_URL):
    query_string = "?" + "&".join(f"{k}={v}" for k, v in params.items())
    return base_url + path + query_string


async def create_address(data: dict, headers: Mapping = {}):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(build_url("locations/addresses/"), json=data) as resp:
            return resp
