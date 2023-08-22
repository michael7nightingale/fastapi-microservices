from fastapi import APIRouter, Depends, Request

from .dependencies import get_city_service, get_country_service


router = APIRouter(prefix="/locations")


@router.get("/cities")
async def cities(
    request: Request,
    city_service=Depends(get_city_service)
):
    cities_list = await city_service.all()
    return cities_list


@router.get("/countries")
async def cities(
    request: Request,
    country_service=Depends(get_country_service)
):
    countries_list = await country_service.all()
    return countries_list
