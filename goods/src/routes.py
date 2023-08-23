from fastapi import APIRouter, Depends, Request, Body
from fastapi.responses import JSONResponse

from .dependencies import get_order_service
from .datasructures import Order, OrderCreate
from .permissions import permission_required

router = APIRouter(prefix="/locations")
