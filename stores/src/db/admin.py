from sqladmin import ModelView, Admin
from starlette.middleware import Middleware

from .models import Store, StoreGood, Post, Employee
from ..middleware import AuthenticationMiddleware


class StoreView(ModelView, model=Store):
    column_list = [
        Store.id, Store.address
    ]


class StoreGoodView(ModelView, model=StoreGood):
    column_list = [
        StoreGood.id, StoreGood.store, StoreGood.good, StoreGood.amount
    ]


class PostView(ModelView, model=Post):
    column_list = [
        Post.id, Post.title, Post.min_salary, Post.max_salary,
    ]


class EmployeeView(ModelView, model=Employee):
    column_list = [
        Employee.id, Employee.store, Employee.first_name, Employee.last_name,
        Employee.email, Employee.post, Employee.salary
    ]


def register_views(app, engine):
    admin = Admin(app=app, engine=engine, middlewares=[Middleware(AuthenticationMiddleware)])
    views = [StoreView, StoreGoodView, PostView, EmployeeView]
    for view in views:
        admin.add_view(view)
