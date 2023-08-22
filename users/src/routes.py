from fastapi import Request, APIRouter, Body, Depends
from fastapi.responses import JSONResponse
from fastapi_authtools.models import EmailPasswordToken
from fastapi_authtools.exceptions import raise_invalid_credentials

from .datasructures import UserModel, UserRegister
from .dependencies import get_user_service


router = APIRouter(prefix="/users")


@router.post("/token")
async def user_home(
    request: Request,
    token_data: EmailPasswordToken = Body(),
    user_service=Depends(get_user_service)
):
    user = await user_service.login(**token_data.model_dump())
    if user is None:
        raise raise_invalid_credentials()
    user_model = UserModel(**user.as_dict())
    access_token = request.app.state.auth_manager.create_token(user_model)
    return {"access-token": access_token}


@router.post("/register")
async def user_home(
    request: Request,
    user_data: UserRegister = Body(),
    user_service=Depends(get_user_service)
):
    user = await user_service.create(**user_data.model_dump())
    if user is None:
        return JSONResponse(
            {"detail": "User with such email already exists."},
            400
        )
    return user
