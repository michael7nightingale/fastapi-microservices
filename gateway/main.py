from fastapi import Request, Body
from fastapi_authtools.models import EmailPasswordToken

from core import GateWay
from config import Settings
from datastructures.users import UserRegister, Token, TokenCreate
from datastructures.locations import City, CityCreate, CountryCreate, Country

app = GateWay()


@app.post(
    path="/users/register",
    service_base_url=Settings().USER_SERVICE_URL,
    response_model=UserRegister,
    body_key="user_data"
)
async def register(request: Request, user_data: UserRegister = Body()):
    pass


@app.post(
    path="/users/token",
    service_base_url=Settings().USER_SERVICE_URL,
    response_model=TokenCreate,
    body_key="token_data"
)
async def register(request: Request, token_data: EmailPasswordToken = Body()):
    pass


@app.get(
    path="/locations/cities",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
    response_model=list[City],
)
async def cities(request: Request):
    pass


@app.post(
    path="/locations/cities",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
    response_model=City,
    body_key="city_data"
)
async def create_city(request: Request, city_data: CityCreate = Body()):
    pass


@app.delete(
    path="/locations/cities/{city_id}",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
)
async def delete_city(request: Request):
    pass


@app.get(
    path="/locations/countries",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
    response_model=list[Country],
)
async def countries(request: Request):
    pass


@app.post(
    path="/locations/countries",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
    response_model=Country,
    body_key="country_data"
)
async def create_country(request: Request, country_data: CountryCreate = Body()):
    pass


@app.delete(
    path="/locations/countries/{country_id}",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
)
async def delete_country(request: Request):
    pass
