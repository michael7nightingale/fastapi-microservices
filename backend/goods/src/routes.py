from fastapi import APIRouter, Depends, Request, Body
from fastapi.responses import JSONResponse
from fastapi_authtools import login_required

from .dependencies import (
    get_company_repository, get_company, get_description_tag,
    get_category, get_category_repository,
    get_subcategory, get_subcategory_repository,
    get_good, get_good_repository,
    get_description_tag_repository,
    get_basket_repository,
    get_order_repository, get_basket_good_repository,

)
from .datasructures import (
    Company,
    Category, CategoryFull,
    Subcategory, SubcategoryFull,
    Good, GoodCreate, GoodFull,
    DescriptionTag, DescriptionTagCreate, DescriptionTagUpdate, BasketGood, OrderCreate, Order, OrderFull,
    BasketGoodCreate, BasketGoodUpdate, BasketFull,

)
from .permissions import permission_required


router = APIRouter(prefix="/goods")


# ============================== COMPANIES ============================ #

@router.get("/companies", response_model=list[Company])
async def companies(company_repository=Depends(get_company_repository)):
    return await company_repository.all()


@router.get("/companies/{company_id}", response_model=Company)
@permission_required(is_superuser=True)
async def company(
    request: Request,
    company_=Depends(get_company),
):
    return company_


# ============================== CATEGORIES ============================ #

@router.get("/categories", response_model=list[Category])
async def categories(category_repository=Depends(get_category_repository)):
    return await category_repository.all()


@router.get("/categories/{category_id}", response_model=CategoryFull)
async def category(
    request: Request,
    category_=Depends(get_category),
):
    return category_


@router.get("/categories/{category_id}/goods", response_model=list[GoodFull])
async def category_goods(
    request: Request,
    category_=Depends(get_category),
    good_repository=Depends(get_good_repository),
):
    return await good_repository.get_goods_by_category(category_['id'])


# ============================== SUBCATEGORIES ============================ #

@router.get("/subcategories", response_model=list[Subcategory])
async def subcategories(subcategory_repository=Depends(get_subcategory_repository)):
    return await subcategory_repository.all()


@router.get("/subcategories/{subcategory_id}", response_model=SubcategoryFull)
async def subcategory(
    request: Request,
    subcategory_=Depends(get_subcategory),
):
    return subcategory_


@router.get("/subcategories/{subcategory_id}/goods", response_model=list[GoodFull])
async def subcategory_goods(
    request: Request,
    subcategory_=Depends(get_subcategory),
    good_repository=Depends(get_good_repository),
):
    return await good_repository.get_goods_by_subcategory(subcategory_['id'])


# ============================== GOODS ============================ #

@router.get("/goods", response_model=list[GoodFull])
async def goods(good_repository=Depends(get_good_repository)):
    return await good_repository.get_goods_with_category_and_subcategory()


@router.post("/goods", response_model=Good)
@permission_required(is_superuser=True)
async def goods(
    request: Request,
    good_repository=Depends(get_good_repository),
    description_tag_repository=Depends(get_description_tag_repository),
    good_data: GoodCreate = Body()
):
    new_good = await good_repository.create(**good_data.model_dump())
    for description_tag in good_data.description_tags:
        await description_tag_repository.create(**description_tag.model_dump())
    return new_good


@router.get("/goods/{good_id}", response_model=GoodFull)
async def good(
    request: Request,
    good_=Depends(get_good),
):
    return good_


@router.get("/goods/{good_id}/description-tags", response_model=list[DescriptionTag])
async def good_description_tags(
    request: Request,
    good_id: str,
    description_tag_repository=Depends(get_description_tag_repository),
):
    return await description_tag_repository.filter(good=good_id)


@router.post("/goods/{good_id}/description-tags", response_model=list[DescriptionTag])
async def good_description_tags(
    request: Request,
    good_id: str,
    description_tag_repository=Depends(get_description_tag_repository),
    description_tag_data: DescriptionTagUpdate = Body()
):
    if description_tag_data.good != good_id:
        return JSONResponse(
            {"detail": "Good id in path and body should match!"},
            status_code=400
        )
    return await description_tag_repository.create(**description_tag_data.model_dump())


@router.patch("/description-tags/{description_tag_id}", response_model=DescriptionTag)
async def description_tag(
    request: Request,
    description_tag_id: str,
    description_tag_=Depends(get_description_tag),
    description_tag_repository=Depends(get_description_tag_repository),
    description_tag_data: DescriptionTagUpdate = Body()
):
    await description_tag_repository.update(description_tag_id, True, **description_tag_data.model_dump())
    return description_tag_


@router.delete("/description-tags/{description_tag_id}", response_model=DescriptionTag)
async def description_tag(
    request: Request,
    description_tag_id: str,
    description_tag_=Depends(get_description_tag),
    description_tag_repository=Depends(get_description_tag_repository),
):
    await description_tag_repository.delete(description_tag_id)
    return {"detail": "Description tag deleted"}


@router.get("/baskets/current", response_model=BasketFull)
@login_required
async def basket(
        request: Request,
        basket_repository=Depends(get_basket_repository)
):
    return await basket_repository.get_basket_with_goods_by_user(request.user.id)


@router.post("/orders", response_model=Order)
@login_required
async def orders(
        request: Request,
        order_repository=Depends(get_order_repository),
        order_data: OrderCreate = Body(),
):
    order_ = order_repository.create_order(**order_data.model_dump())
    if order_ is None:
        return JSONResponse(
            {'detail': "Data is invalid!"},
            status_code=400
        )
    return order_


@router.get("/orders/{order_id}", response_model=OrderFull)
@login_required
async def order(
        request: Request,
        order_id: str,
        order_repository=Depends(get_order_repository),
        order_data: OrderCreate = Body(),
):
    order_ = order_repository.get_order_by_id_and_user(
        id_=order_id,
        user_id=request.user.id
    )
    if order_ is None:
        return JSONResponse(
            {'detail': "Order does not exists!"},
            status_code=404
        )
    return order_


@router.post("/baskets/current/goods", response_model=BasketGood)
@login_required
async def basket_goods(
        request: Request,
        basket_good_repository=Depends(get_basket_good_repository),
        basket_good_data: BasketGoodCreate = Body(),
):
    basket_good_ = await basket_good_repository.create_basket_good(
        **basket_good_data.model_dump(),
        user=request.user.id
    )
    if basket_good_ is None:
        return JSONResponse(
            {'detail': "Data is invalid!"},
            status_code=400
        )
    return basket_good_


@router.delete("/baskets/current/goods/{basket_good_id}", response_model=BasketGood)
@login_required
async def basket_good(
        request: Request,
        basket_good_id: str,
        basket_good_repository=Depends(get_basket_good_repository),
):
    await basket_good_repository.delete_basket(
        basket_good_id, user=request.user.id
    )
    return JSONResponse(
        {"detail": "Basket good deleted."}
    )


@router.patch("/baskets/current/goods/{basket_good_id}", response_model=BasketGood)
@login_required
async def basket_good(
        request: Request,
        basket_good_id: str,
        basket_good_repository=Depends(get_basket_good_repository),
        basket_good_data: BasketGoodUpdate = Body()
):
    await basket_good_repository.update_basket(
        values=basket_good_data.model_dump(),
        id_=basket_good_id, user=request.user.id
    )
    return JSONResponse(
        {"detail": "Basket good updates."}
    )
