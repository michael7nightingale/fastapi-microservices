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


class Address(BaseModel):
    id: str
    city: str
    street: str
    number: str


class AddressCreate(BaseModel):
    city: str
    street: str
    number: str


class AddressUpdate(BaseModel):
    city: str | None = None
    street: str | None = None
    number: str | None = None


class UserModel(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool = False
    is_staff: bool = False
