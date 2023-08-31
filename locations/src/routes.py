from fastapi import APIRouter, Depends, Request, Body
from fastapi.responses import JSONResponse

from .dependencies import (
    get_city_service, get_city,
    get_country_service, get_country,
    get_address, get_address_service
)
from .datasructures import City, Country, Address, AddressCreate, AddressUpdate
from .permissions import permission_required


router = APIRouter(prefix="/locations")


# =============================== CITIES ============================= #

@router.get("/cities", response_model=list[City])
async def cities(
    request: Request,
    city_service=Depends(get_city_service)
):
    cities_list = await city_service.all()
    return cities_list


# =============================== COUNTRIES ============================= #

@router.get("/countries", response_model=list[Country])
async def countries(
    request: Request,
    country_service=Depends(get_country_service)
):
    countries_list = await country_service.all()
    return countries_list


@router.get("/countries/{country_id}", response_model=Country)
async def country(
    request: Request,
    country_service=Depends(get_country_service),
    country_=Depends(get_country),
):
    return country_


# =============================== ADDRESSES ============================= #

@router.post("/addresses", response_model=Address)
async def create_address(
    request: Request,
    address_data: AddressCreate = Body(),
    address_service=Depends(get_address_service)
):
    address = await address_service.create(**address_data.model_dump())
    if address is None:
        return JSONResponse(
            "Invalid data to address creation",
            400
        )
    return address


@router.get("/addresses/{address_id}", response_model=Address)
async def address(
    request: Request,
    address_id: str,
    address_=Depends(get_address),
    address_service=Depends(get_address_service)
):
    return address_


@router.patch("/addresses/{address_id}", response_model=Address)
async def address(
    request: Request,
    address_id: str,
    address_=Depends(get_address),
    address_data: AddressUpdate = Body(),
    address_service=Depends(get_address_service)
):
    await address_service.update(address_.id, **address_data.model_dump())
    return address_


@router.delete("/addresses/{address_id}")
async def address(
    request: Request,
    address_id: str,
    address_=Depends(get_address),
    address_service=Depends(get_address_service)
):
    await address_service.delete(address_.id)
    return {"Address is deleted successfully."}
