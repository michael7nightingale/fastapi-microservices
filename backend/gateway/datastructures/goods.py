from pydantic import BaseModel, Field


class CompanyCreate(BaseModel):
    title: str
    description: str
    country: str


class CompanyUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    country: str | None = None


class Company(BaseModel):
    id: str
    title: str
    description: str
    country: str


class CategoryCreate(BaseModel):
    title: str


class CategoryUpdate(BaseModel):
    title: str | None = None


class Category(BaseModel):
    id: str
    title: str


class SubcategoryCreate(BaseModel):
    title: str
    category: str


class SubcategoryUpdate(BaseModel):
    title: str | None = None
    category: str | None = None


class Subcategory(BaseModel):
    id: str
    title: str
    category: str


class DescriptionTagCreate(BaseModel):
    good: str
    tag: str
    text: str


class GoodCreate(BaseModel):
    title: str
    description: str
    subcategory: str
    price: int
    discount: int
    # company: str
    description_tags: list[DescriptionTagCreate] = Field(default_factory=list)


class GoodUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    subcategory: str | None = None
    price: int | None = None
    discount: int | None = None


class Good(BaseModel):
    id: str
    title: str
    description: str
    subcategory: str
    price: int
    discount: int
    # company: str


class DescriptionTagUpdate(BaseModel):
    good: str | None = None
    tag: str | None = None
    text: str | None = None


class DescriptionTag(BaseModel):
    id: str
    good: str
    tag: str
    text: str
