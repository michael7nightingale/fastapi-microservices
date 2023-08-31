from functools import wraps
from typing import Awaitable

from fastapi import Request, HTTPException


def permission_required(**conditions):
    """Decorator to check user permissions for endpoint."""
    def wrapped(func):

        @wraps(func)
        async def inner(request: Request, *args, **kwargs):
            print(request.user)
            if request.user is not None:
                if all((getattr(request.user, k) == v for k, v in conditions.items())):
                    res = func(request, *args, **kwargs)
                    if isinstance(res, Awaitable):
                        res = await res
                    return res
            raise HTTPException(
                detail="You have no the permission.",
                status_code=403
            )
        return inner
    return wrapped
