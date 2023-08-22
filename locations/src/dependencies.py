from fastapi import Depends, Request, HTTPException

from .db.services import CityService, CountryService


def get_pool(request: Request):
    return request.app.state.pool


async def get_session(pool=Depends(get_pool)):
    async with pool() as session:
        yield session


def get_service(service_class):
    def inner(session=Depends(get_session)):
        return service_class(session)
    return inner


get_city_service = get_service(CityService)
get_country_service = get_service(CountryService)


async def get_country(country_id: str, country_service: CountryService = Depends(get_country_service)):
    country = await country_service.get(country_id)
    if country is None:
        raise HTTPException(
            detail="Country is not found.",
            status_code=404
        )
    return country


async def get_city(city_id: str, city_service: CityService = Depends(get_city_service)):
    city = await city_service.get(city_id)
    if city is None:
        raise HTTPException(
            detail="City is not found.",
            status_code=404
        )
    return city
