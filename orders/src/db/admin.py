from sqladmin import ModelView, Admin
from starlette.middleware import Middleware

from .models import Order, Basket, BasketGood
from ..middleware import AuthenticationMiddleware


class OrderView(ModelView, model=Order):
    column_list = [
        Order.id, Order.basket, Order.user, Order.address, Order.time_finished,
        Order.time_created, Order.is_paid
    ]


class BasketView(ModelView, model=Basket):
    column_list = [
        Basket.id, Basket.user, Basket.current
    ]


class BasketGoodView(ModelView, model=BasketGood):
    column_list = [
        BasketGood.id, BasketGood.basket, BasketGood.amount, BasketGood.good,
    ]


def register_views(app, engine):
    admin = Admin(app=app, engine=engine, middlewares=[Middleware(AuthenticationMiddleware)])
    views = [OrderView, BasketGoodView, BasketGoodView]
    for view in views:
        admin.add_view(view)
