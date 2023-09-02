from sqladmin import ModelView, Admin
from starlette.middleware import Middleware

from ..db.models import Good, Subcategory, Category, Company, DescriptionTag
from ..middleware import AuthenticationMiddleware


class GoodView(ModelView, model=Good):
    column_list = [
        Good.id, Good.title, Good.description,
        Good.price, Good.discount,
        Good.subcategory
    ]


class CategoryView(ModelView, model=Category):
    column_list = [
        Category.id, Category.title
    ]


class SubcategoryView(ModelView, model=Subcategory):
    column_list = [
        Subcategory.id, Subcategory.title, Subcategory.category
    ]


class CompanyView(ModelView, model=Company):
    column_list = [
        Company.id, Company.title, Company.description, Company.country
    ]


class DescriptionTagView(ModelView, model=DescriptionTag):
    column_list = [
        DescriptionTag.id, DescriptionTag.tag, DescriptionTag.text, DescriptionTag.good
    ]


def register_views(app, engine):
    admin = Admin(app=app, engine=engine, middlewares=[Middleware(AuthenticationMiddleware)])
    views = [CompanyView, CategoryView, SubcategoryView, GoodView, DescriptionTagView]
    for view in views:
        admin.add_view(view)
