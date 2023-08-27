from fastapi import APIRouter, Depends, Request, Body
from fastapi.responses import JSONResponse

from .connectors import create_address
from .datasructures import StoreCreate, Store, Employee, EmployeeCreate, PostCreate, Post, Address
from .dependencies import get_store_service, get_post_service, get_employee_service
from .permissions import permission_required


router = APIRouter()


@router.get("/stores", response_model=list[Store])
async def stores(
    request: Request,
    store_service=Depends(get_store_service)
):
    stores_list = await store_service.all()
    return stores_list


@router.post("/stores", response_model=Store)
@permission_required(is_superuser=True)
async def create_store(
    request: Request,
    store_data: StoreCreate = Body(),
    store_service=Depends(get_store_service)
):
    address_create_response = await create_address(
        store_data.address.model_dump(),
        headers=request.headers
    )
    if not address_create_response:
        return address_create_response.json()
    address = Address(**(await address_create_response.json()))
    new_store = await store_service.create(address=address.id)
    return new_store


@router.get("/posts", response_model=list[Post])
@permission_required(is_staff=True)
async def posts(
    request: Request,
    post_service=Depends(get_post_service)
):
    posts_list = await post_service.all()
    return posts_list


@router.post("/posts", response_model=Post)
@permission_required(is_superuser=True)
async def create_post(
    request: Request,
    post_data: PostCreate = Body(),
    post_service=Depends(get_post_service)
):
    new_post = await post_service.create(**post_data.model_dump())
    return new_post


@router.get("/employees", response_model=list[Employee])
@permission_required(is_staff=True)
async def employees(
    request: Request,
    employee_service=Depends(get_employee_service)
):
    employees_list = await employee_service.all()
    return employees_list


@router.post("/employees", response_model=Employee)
@permission_required(is_superuser=True)
async def create_employee(
    request: Request,
    employee_data: EmployeeCreate = Body(),
    employee_service=Depends(get_employee_service)
):
    new_employee = await employee_service.create(**employee_data.model_dump())
    return new_employee
