from sqladmin import ModelView, Admin
from starlette.middleware import Middleware

from .models import City, Country, Address
from ..middleware import AuthenticationMiddleware


class CityView(ModelView, model=City):
    column_list = [
        City.id, City.country, City.name
    ]


class CountryView(ModelView, model=Country):
    column_list = [
        Country.id, Country.name
    ]


class AddressView(ModelView, model=Address):
    column_list = [
        Address.id, Address.city, Address.street, Address.number,
    ]


def register_views(app, engine):
    admin = Admin(app=app, engine=engine, middlewares=[Middleware(AuthenticationMiddleware)])
    views = [CityView, CountryView, AddressView]
    for view in views:
        admin.add_view(view)
