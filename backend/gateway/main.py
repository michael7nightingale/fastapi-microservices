from fastapi import Request, Body
from fastapi_authtools.models import EmailPasswordToken

from admin.routes import admin_router
from middleware import register_middleware
from core import GateWay
from config import Settings
from datastructures.users import UserRegister, Token, TokenCreate, UserModel
from datastructures.locations import City, CityCreate, CountryCreate, Country, AddressCreate, Address
from datastructures.stores import Store
from datastructures.goods import GoodFull, Category, Subcategory, CategoryFull, SubcategoryFull, DescriptionTag


app = GateWay()


# =============================== USERS ================================ #

@app.post(
    path="/users/register",
    service_base_url=Settings().USER_SERVICE_URL,
    response_model=UserModel,
    body_key="user_data"
)
async def register(request: Request, user_data: UserRegister = Body()):
    pass


@app.post(
    path="/users/token",
    service_base_url=Settings().USER_SERVICE_URL,
    response_model=Token,
    body_key="token_data"
)
async def register(request: Request, token_data: EmailPasswordToken = Body()):
    pass


@app.post(
    path="/users/me",
    service_base_url=Settings().USER_SERVICE_URL,
    response_model=UserModel,
)
async def register(request: Request):
    pass


# =============================== LOCATIONS ================================ #

@app.get(
    path="/locations/cities",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
    response_model=list[City],
)
async def cities(request: Request):
    pass


@app.get(
    path="/locations/countries",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
    response_model=list[Country],
)
async def countries(request: Request):
    pass


@app.get(
    path="/locations/addresses/{address_id}",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
    response_model=Address,
)
async def address(request: Request):
    pass


@app.post(
    path="/locations/addresses",
    service_base_url=Settings().LOCATIONS_SERVICE_URL,
    response_model=Address,
    body_key="address_data"
)
async def addresses(request: Request, address_data: AddressCreate = Body()):
    pass


# =============================== STORES ================================ #

@app.get(
    path="/stores",
    service_base_url=Settings().STORES_SERVICE_URL,
    response_model=Store,
    response_list=True
)
async def stores(
    request: Request,
):
    pass


# ============================= GOODS =========================== #

@app.get(
    path="/goods/categories",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=Category,
    response_list=True
)
async def categories(request: Request):
    pass


@app.get(
    path="/goods/categories/{category_id}",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=CategoryFull,
)
async def category(request: Request):
    pass


@app.get(
    path="/goods/categories/{category_id}/goods",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=GoodFull,
    response_list=True
)
async def goods_by_category(request: Request):
    pass


@app.get(
    path="/goods/subcategories",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=Subcategory,
    response_list=True
)
async def subcategories(request: Request):
    pass


@app.get(
    path="/goods/subcategories/{subcategory_id}",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=SubcategoryFull,
)
async def subcategory(request: Request):
    pass


@app.get(
    path="/goods/subcategories/{subcategory_id}/goods",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=GoodFull,
    response_list=True
)
async def goods_by_subcategory(request: Request):
    pass


@app.get(
    path="/goods/goods/{good_id}",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=GoodFull,
)
async def good(request: Request):
    pass


@app.get(
    path="/goods/goods",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=GoodFull,
    response_list=True
)
async def goods(request: Request):
    pass


@app.get(
    path="/goods/goods/{good_id}",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=GoodFull,
)
async def good(request: Request):
    pass


@app.get(
    path="/goods/goods/{good_id}/description-tags",
    service_base_url=Settings().GOODS_SERVICE_URL,
    response_model=DescriptionTag,
    response_list=True
)
async def good_description_tags(request: Request):
    pass


app.include_router(admin_router)
register_middleware(app)
