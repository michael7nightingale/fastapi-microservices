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