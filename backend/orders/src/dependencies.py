from fastapi import Depends, Request, HTTPException

from .db.services import OrderService, BasketGoodService, BasketService


def get_pool(request: Request):
    return request.app.state.pool


async def get_session(pool=Depends(get_pool)):
    async with pool() as session:
        yield session


def get_service(service_class):
    def inner(session=Depends(get_session)):
        return service_class(session)
    return inner


get_order_service = get_service(OrderService)
get_basket_service = get_service(BasketService)
get_basket_goods_service = get_service(BasketGoodService)


async def get_order(request: Request, order_id: str, order_service=Depends(get_order_service)):
    order = await order_service.get(order_id, user=request.user.id)
    if order is None:
        raise HTTPException(
            404,
            "There is no such order.",
        )
    return order


async def get_basket(request: Request, basket_service=Depends(get_basket_service)):
    basket = await basket_service.get(user=request.user.id, current=True)
    if basket is None:
        new_basket = await basket_service.create(user=request.user.id, current=True)
        return new_basket
    return basket


async def get_basket_goods(
        basket=Depends(get_basket),
        basket_goods_service=Depends(get_basket_goods_service)
):
    basket_goods = await basket_goods_service.filter(basket=basket.id)
    return basket_goods


async def get_basket_good(
        basket_good_id: str,
        basket=Depends(get_basket),
        basket_goods_service=Depends(get_basket_goods_service)
):
    basket_good = await basket_goods_service.get(basket=basket.id, id=basket_good_id)
    if basket_good is None:
        raise HTTPException(
            404,
            "There is no such basket good.",
        )
    return basket_good
