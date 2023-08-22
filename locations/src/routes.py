from fastapi import APIRouter, Depends, Request, Body
from fastapi.responses import JSONResponse

from .dependencies import get_city_service, get_country_service, get_country, get_city
from .datasructures import CityCreate, City, Country, CountryCreate
from .permissions import permission_required

router = APIRouter(prefix="/locations")


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


@router.get("/countries")
async def cities(
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
