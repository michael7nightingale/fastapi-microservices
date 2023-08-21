import aiohttp


async def make_request(
    method: str,
    url: str,
    headers: dict = {},
    data: dict = {}
) -> dict:
    """Async i/o request method"""
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.request(method=method, url=url, json=data) as response:
            data = await response.json()
            return data
