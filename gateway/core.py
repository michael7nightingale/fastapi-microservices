from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Callable, Type
from functools import wraps

from connector import make_request


class GateWay(FastAPI):
    """
    Gateway FastAPI class to get response from services.
    """

    def route(
        self,
        method: str,
        path: str,
        service_base_url: str,
        response_model: Type[BaseModel] | None = None,
        body_key: str | None = None,
    ):
        if not (path[0] == "/" and path[:2] != "//"):
            raise ValueError("Path must start with a single slash `/`.")
        app_route_decorator = getattr(super(), method)

        def wrapper(func: Callable):
            @app_route_decorator(path)
            @wraps(func)
            async def inner(request: Request, **kwargs):
                """Request to service """
                if body_key:
                    data = kwargs.get(body_key).model_dump()
                else:
                    data = None
                service_url = service_base_url + str(request.url.path)

                response_data = await make_request(
                    method=method,
                    url=service_url,
                    data=data,
                )
                if response_model:
                    response_data = response_model(**response_data)
                return response_data

            return inner
        return wrapper

    def get(self, **kwargs):
        return self.route(method="get", **kwargs)

    def post(self, **kwargs):
        return self.route(method="post", **kwargs)

    def delete(self, **kwargs):
        return self.route(method="delete", **kwargs)

    def put(self, **kwargs):
        return self.route(method="put", **kwargs)

    def patch(self, **kwargs):
        return self.route(method="patch", **kwargs)
