import aiohttp


async def make_request(
    method: str,
    url: str,
    headers: dict = {},
    data: dict = {},
) -> dict:
    """Async i/o request method"""
    headers_ = {}
    if "Authorization" in headers:
        headers_['Authorization'] = headers['Authorization']
    if "authorization" in headers:
        headers_['authorization'] = headers['authorization']
    async with aiohttp.ClientSession(headers=headers_) as session:
        async with session.request(method=method, url=url, json=data) as response:
            data = await response.json()
            return data
