from fastapi import APIRouter, Depends, Request, Body
from fastapi.responses import JSONResponse

from .dependencies import (
    get_company_service, get_company, get_description_tag,
    get_category, get_category_service,
    get_subcategory, get_subcategory_service,
    get_good, get_good_service,
    get_description_tag_service

)
from .datasructures import (
    Company, CompanyCreate, CompanyUpdate,
    Category, CategoryCreate, CategoryUpdate,
    Subcategory, SubcategoryCreate, SubcategoryUpdate,
    Good, GoodCreate, GoodUpdate,
    DescriptionTag, DescriptionTagCreate, DescriptionTagUpdate,

)
from .permissions import permission_required


router = APIRouter(prefix="/goods")


# ============================== COMPANIES ============================ #

@router.get("/companies", response_model=list[Company])
async def companies(company_service=Depends(get_company_service)):
    return await company_service.all()


@router.get("/companies/{company_id}", response_model=Company)
@permission_required(is_superuser=True)
async def company(
    request: Request,
    company_=Depends(get_company),
):
    return company_


# ============================== CATEGORIES ============================ #

@router.get("/categories", response_model=list[Category])
async def categories(category_service=Depends(get_category_service)):
    return await category_service.all()


@router.get("/categories/{category_id}", response_model=Category)
@permission_required(is_superuser=True)
async def category(
    request: Request,
    category_=Depends(get_category),
):
    return category_


# ============================== SUBCATEGORIES ============================ #

@router.get("/subcategories", response_model=list[Subcategory])
async def subcategories(subcategory_service=Depends(get_subcategory_service)):
    return await subcategory_service.all()


@router.get("/subcategories/{subcategory_id}", response_model=Subcategory)
@permission_required(is_superuser=True)
async def subcategory(
    request: Request,
    subcategory_=Depends(get_subcategory),
):
    return subcategory_


# ============================== GOODS ============================ #

@router.get("/goods", response_model=list[Good])
async def goods(good_service=Depends(get_good_service)):
    return await good_service.all()


@router.post("/goods", response_model=Good)
@permission_required(is_superuser=True)
async def goods(
    request: Request,
    good_service=Depends(get_good_service),
    description_tag_service=Depends(get_description_tag_service),
    good_data: GoodCreate = Body()
):
    new_good = await good_service.create(**good_data.model_dump())
    for description_tag in good_data.description_tags:
        await description_tag_service.create(**description_tag.model_dump())
    return new_good


@router.get("/goods/{good_id}", response_model=Good)
async def good(
    request: Request,
    good_=Depends(get_good),
):
    return good_


@router.get("/goods/{good_id}/description-tags", response_model=list[DescriptionTag])
async def good_description_tags(
    request: Request,
    good_id: str,
    description_tag_service=Depends(get_description_tag_service),
):
    return await description_tag_service.filter(good=good_id)


@router.post("/goods/{good_id}/description-tags", response_model=list[DescriptionTag])
async def good_description_tags(
    request: Request,
    good_id: str,
    description_tag_service=Depends(get_description_tag_service),
    description_tag_data: DescriptionTagUpdate = Body()
):
    if description_tag_data.good != good_id:
        return JSONResponse(
            {"detail": "Good id in path and body should match!"},
            status_code=400
        )
    return await description_tag_service.create(**description_tag_data.model_dump())


@router.patch("/description-tags/{description_tag_id}", response_model=DescriptionTag)
async def description_tag(
    request: Request,
    description_tag_id: str,
    description_tag_=Depends(get_description_tag),
    description_tag_service=Depends(get_description_tag_service),
    description_tag_data: DescriptionTagUpdate = Body()
):
    await description_tag_service.update(description_tag_id, True, **description_tag_data.model_dump())
    return description_tag_


@router.delete("/description-tags/{description_tag_id}", response_model=DescriptionTag)
async def description_tag(
    request: Request,
    description_tag_id: str,
    description_tag_=Depends(get_description_tag),
    description_tag_service=Depends(get_description_tag_service),
):
    await description_tag_service.delete(description_tag_id)
    return {"detail": "Description tag deleted"}
