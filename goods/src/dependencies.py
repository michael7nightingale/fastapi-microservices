from fastapi import Depends, Request, HTTPException

from .db.models import Company, Category, Subcategory, Good, DescriptionTag
from .db.services import GoodService, DescriptionTagService, CategoryService, SubcategoryService, CompanyService


def get_pool(request: Request):
    return request.app.state.pool


async def get_session(pool=Depends(get_pool)):
    async with pool() as session:
        yield session


def get_service(service_class):
    def inner(session=Depends(get_session)):
        return service_class(session)
    return inner


get_good_service = get_service(GoodService)
get_company_service = get_service(CompanyService)
get_category_service = get_service(CategoryService)
get_subcategory_service = get_service(SubcategoryService)
get_description_tag_service = get_service(DescriptionTagService)


async def get_company(
        company_id: str,
        company_service=Depends(get_company_service)
) -> Company | None:
    company = await company_service.get_or_none(company_id)
    if company is None:
        raise HTTPException(
            detail="Company does not exists.",
            status_code=404
        )
    return company


async def get_category(
        category_id: str,
        category_service=Depends(get_category_service)
) -> Category | None:
    category = await category_service.get_or_none(category_id)
    if category is None:
        raise HTTPException(
            detail="Category does not exists.",
            status_code=404
        )
    return category


async def get_subcategory(
        subcategory_id: str,
        subcategory_service=Depends(get_subcategory_service)
) -> Subcategory | None:
    subcategory = await subcategory_service.get_or_none(subcategory_id)
    if subcategory is None:
        raise HTTPException(
            detail="Subcategory does not exists.",
            status_code=404
        )
    return subcategory


async def get_good(
        good_id: str,
        good_service=Depends(get_good_service)
) -> Good | None:
    good = await good_service.get_or_none(good_id)
    if good is None:
        raise HTTPException(
            detail="Good does not exists.",
            status_code=404
        )
    return good


async def get_description_tag(
        description_tag_id: str,
        description_tag_service=Depends(get_description_tag_service)
) -> DescriptionTag | None:
    description_tag = await description_tag_service.get_or_none(description_tag_id)
    if description_tag is None:
        raise HTTPException(
            detail="Description tag does not exists.",
            status_code=404
        )
    return description_tag
