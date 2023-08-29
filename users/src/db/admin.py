from sqladmin import ModelView, Admin
from starlette.middleware import Middleware

from .models import User
from ..middleware import AuthenticationMiddleware


class UserView(ModelView, model=User):
    column_list = [
        User.id, User.last_name, User.first_name,
        User.email, User.is_staff, User.is_superuser
    ]


def register_views(app, engine):
    admin = Admin(app=app, engine=engine, middlewares=[Middleware(AuthenticationMiddleware)])
    views = [UserView]
    for view in views:
        admin.add_view(view)
