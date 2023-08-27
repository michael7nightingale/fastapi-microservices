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


class AddressCreate(BaseModel):
    city: str
    street: str
    number: str


class Address(BaseModel):
    id: str
    city: str
    street: str
    number: str
