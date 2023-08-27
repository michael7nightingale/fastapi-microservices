from fastapi import APIRouter, Depends, Request, Body
from fastapi.responses import JSONResponse

from .dependencies import (
    get_city_service, get_city,
    get_country_service, get_country,
    get_address, get_address_service
)
from .datasructures import CityCreate, City, Country, CountryCreate, Address, AddressCreate
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


@router.post("/cities", response_model=City)
# @permission_required(is_superuser=True)
async def create_city(
    request: Request,
    city_data: CityCreate = Body(),
    city_service=Depends(get_city_service)
):
    city = await city_service.create(**city_data.model_dump())
    if city is None:
        return JSONResponse(
            "Invalid data to city creation",
            400
        )
    return city


@router.delete("/cities/{city_id}")
@permission_required(is_superuser=True)
async def delete_city(
    request: Request,
    city_id: str,
    city=Depends(get_city),
    city_service=Depends(get_city_service)
):
    await city_service.delete(city_id)
    return {"detail": f"City {city} is deleted."}


# =============================== COUNTRIES ============================= #

@router.get("/countries")
async def countries(
    request: Request,
    country_service=Depends(get_country_service)
):
    countries_list = await country_service.all()
    return countries_list


@router.post("/countries", response_model=Country)
@permission_required(is_superuser=True)
async def create_country(
    request: Request,
    country_data: CountryCreate = Body(),
    country_service=Depends(get_country_service)
):
    country = await country_service.create(**country_data.model_dump())
    if country is None:
        return JSONResponse(
            "Invalid data to city creation",
            400
        )
    return country


@router.delete("/countries/{country_id}")
@permission_required(is_superuser=True)
async def delete_country(
    request: Request,
    country_id: str,
    country=Depends(get_country),
    country_service=Depends(get_country_service)
):
    await country_service.delete(country_id)
    return {"detail": f"Country {country} is deleted."}


# =============================== ADDRESSES ============================= #

@router.get("/addresses", response_model=list[Address])
async def addresses(
    request: Request,
    address_service=Depends(get_address_service)
):
    addresses_list = await address_service.all()
    return addresses_list


@router.post("/addresses", response_model=Address)
@permission_required(is_superuser=True)
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


@router.delete("/addresses/{address_id}")
@permission_required(is_superuser=True)
async def delete_address(
    request: Request,
    address_id: str,
    address=Depends(get_address),
    address_service=Depends(get_address_service)
):
    await address_service.delete(address_id)
    return {"detail": f"Address {address} is deleted."}
