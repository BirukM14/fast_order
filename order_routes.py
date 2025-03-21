from fastapi import APIRouter,Depends
from fastapi _jwt_auth import AuthJWT
from models import User,Order
from schemas import orderModel


order_router = APIRouter()


@order_router.get('/')
async def hello(Authorize:AuthJWT=Depends()):
    

