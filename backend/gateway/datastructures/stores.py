from pydantic import BaseModel


class AddressCreate(BaseModel):
    city: str
    street: str
    number: str


class Address(BaseModel):
    id: str
    city: str
    street: str
    number: str


class StoreCreate(BaseModel):
    address: AddressCreate


class Store(BaseModel):
    id: str
    address: str


class PostCreate(BaseModel):
    title: str
    min_salary: int
    max_salary: int


class Post(BaseModel):
    id: str
    title: str
    min_salary: int
    max_salary: int


class EmployeeCreate(BaseModel):
    post: str
    store: str
    salary: int
    first_name: str
    last_name: str
    email: str


class Employee(BaseModel):
    id: str
    post: str
    store: str
    salary: int
    first_name: str
    last_name: str
    email: str


class EmployeeAdminShow(BaseModel):
    id: str
    post: str
    store: str
    salary: int
    first_name: str
    last_name: str
    email: str
    key: str
