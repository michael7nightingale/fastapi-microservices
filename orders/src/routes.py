from fastapi import APIRouter, Depends, Request, Body
from fastapi.responses import JSONResponse
from fastapi_authtools import login_required

from .dependencies import (
    get_order_service, get_order,
    get_basket,
    get_basket_goods_service, get_basket_goods, get_basket_good

)
from .datasructures import (
    Order, OrderCreate,
    Basket, BasketGood, BasketGoodCreate, BasketGoodUpdate

)
from .connectors import create_address


router = APIRouter(prefix="/orders")


# ================================= BASKETS ============================== #

@router.get("/basket", response_model=Basket)
@login_required
async def basket(
        request: Request,
        basket_=Depends(get_basket)
):
    return basket_


# ================================= BASKET GOODS ============================== #

@router.get("/basket/goods", response_model=list[BasketGood])
@login_required
async def basket_goods(
        request: Request,
        basket_goods_=Depends(get_basket_goods)
):
    return basket_goods_


@router.post("/basket/goods", response_model=BasketGood)
@login_required
async def basket_goods(
        request: Request,
        basket_good_data: BasketGoodCreate = Body(),
        basket_=Depends(get_basket),
        basket_goods_service=Depends(get_basket_goods_service)
):
    basket_good_ = await basket_goods_service.create(**basket_good_data.model_dump(), basket=basket_.id)
    return basket_good_


@router.patch("/basket/goods/{basket_good_id}", response_model=BasketGood)
@login_required
async def basket_good(
        request: Request,
        basket_good_data: BasketGoodUpdate = Body(),
        basket_good_=Depends(get_basket_good),
        basket_goods_service=Depends(get_basket_goods_service)
):
    await basket_goods_service.update(basket_good_.id, **basket_good_data.model_dump())
    return basket_good_


@router.delete("/basket/goods/{basket_good_id}")
@login_required
async def basket_good(
        request: Request,
        basket_good_=Depends(get_basket_good),
        basket_goods_service=Depends(get_basket_goods_service)
):
    await basket_goods_service.delete(basket_good_.id)
    return {"detail": "Order deleted."}


# ================================= ORDERS ============================== #

@router.get("/orders", response_model=list[Order])
@login_required
async def orders(
        request: Request,
        order_service=Depends(get_order_service)
):
    orders_ = await order_service.filter(user=request.user.id)
    return orders_


@router.post("/orders", response_model=Order)
@login_required
async def orders(
        request: Request,
        order_data: OrderCreate = Body(),
        order_service=Depends(get_order_service)
):
    address_response = await create_address(order_data.address.model_dump())
    if not address_response.status:
        return await address_response.json()
    address_response_data = await address_response.json()
    order_ = await order_service.create_order(
        user=request.user.id,
        address=await address_response_data['id'],
        **order_data.model_dump(exclude={"address"}),
    )
    if order_ is None:
        return JSONResponse(
            {"detail": "Cannot create order."},
            status_code=400
        )
    return order_


@router.get("/orders/{order_id}", response_model=list[Order])
@login_required
async def order(
        request: Request,
        order_=Depends(get_order)
):
    return order_


@router.delete("/orders/{order_id}", response_model=list[Order])
@login_required
async def orders(
        request: Request,
        order_=Depends(get_order),
        order_service=Depends(get_order_service)
):
    await order_service.delete(order_.id)
    return {"detail": "Order deleted."}
