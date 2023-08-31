from fastapi import Depends, Request

from .db.services import EmployeeService, PostService, StoreService


def get_pool(request: Request):
    return request.app.state.pool


async def get_session(pool=Depends(get_pool)):
    async with pool() as session:
        yield session


def get_service(service_class):
    def inner(session=Depends(get_session)):
        return service_class(session)
    return inner


get_store_service = get_service(StoreService)
get_post_service = get_service(PostService)
get_employee_service = get_service(EmployeeService)
