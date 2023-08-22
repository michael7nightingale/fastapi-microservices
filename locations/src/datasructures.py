from pydantic import BaseModel


class CityCreate(BaseModel):
    name: str
    country: str


class CountryCreate(BaseModel):
    name: str


class Country(BaseModel):
    id: str
    name: str


class City(BaseModel):
    id: str
    name: str
    country: str


class UserModel(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False
    is_staff: bool = False
