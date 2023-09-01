from fastapi import Form, Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from config import get_settings


templates = Jinja2Templates(directory="admin/templates/")
admin_router = APIRouter(prefix="/admin")


@admin_router.get('/login')
async def admin_login(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('admin_login.html', context)


@admin_router.post('/login')
async def admin_login(request: Request, login: str = Form(), password: str = Form()):   # noqa: F811
    settings = get_settings()
    if settings.SUPERUSER_LOGIN == login and settings.SUPERUSER_PASSWORD == password:
        response = RedirectResponse('/admin', status_code=303)
        response.set_cookie('Authorization', settings.SUPERUSER_TOKEN)
        return response
    else:
        return RedirectResponse(admin_router.url_path_for('admin_login'), status_code=303)
