from fastapi import Depends, Request, HTTPException

from .db.models import Company, Category, Subcategory, Good, DescriptionTag
from .db.repositories import (
    GoodRepository,
    DescriptionTagRepository,
    CategoryRepository,
    SubcategoryRepository,
    CompanyRepository,

)


def get_pool(request: Request):
    return request.app.state.pool


async def get_session(pool=Depends(get_pool)):
    async with pool() as session:
        yield session


def get_repository(repository_class):
    def inner(session=Depends(get_session)):
        return repository_class(session)
    return inner


get_good_repository = get_repository(GoodRepository)
get_company_repository = get_repository(CompanyRepository)
get_category_repository = get_repository(CategoryRepository)
get_subcategory_repository = get_repository(SubcategoryRepository)
get_description_tag_repository = get_repository(DescriptionTagRepository)


async def get_company(
        company_id: str,
        company_repository=Depends(get_company_repository)
) -> Company | None:
    company = await company_repository.get(company_id)
    if company is None:
        raise HTTPException(
            detail="Company does not exists.",
            status_code=404
        )
    return company


async def get_category(
        category_id: str,
        category_repository=Depends(get_category_repository)
) -> Category | None:
    category = await category_repository.get_with_subcategories(category_id)
    if category is None:
        raise HTTPException(
            detail="Category does not exists.",
            status_code=404
        )
    return category


async def get_subcategory(
        subcategory_id: str,
        subcategory_repository=Depends(get_subcategory_repository)
) -> Subcategory | None:
    subcategory = await subcategory_repository.get_with_category(subcategory_id)
    if subcategory is None:
        raise HTTPException(
            detail="Subcategory does not exists.",
            status_code=404
        )
    return subcategory


async def get_good(
        good_id: str,
        good_repository=Depends(get_good_repository)
) -> Good | None:
    good = await good_repository.get_good_with_category_and_subcategory(good_id)
    if good is None:
        raise HTTPException(
            detail="Good does not exists.",
            status_code=404
        )
    return good


async def get_description_tag(
        description_tag_id: str,
        description_tag_repository=Depends(get_description_tag_repository)
) -> DescriptionTag | None:
    description_tag = await description_tag_repository.get(description_tag_id)
    if description_tag is None:
        raise HTTPException(
            detail="Description tag does not exists.",
            status_code=404
        )
    return description_tag
