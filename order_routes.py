from fastapi import APIRouter,Depends
from fastapi _jwt_auth import AuthJWT
from models import User,Order
from schemas import orderModel
from fastapi.exceptions import HTTPException
from data


order_router = APIRouter()


@order_router.get('/')
async def hello(Authorize:AuthJWT=Depends()):

    try:
        Authorize.jwt_required()



    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )

    return {"message":"hellow worman"}


@order_router.post('/')

async def place _an_order(order:orderModel,Authorize:AuthJWT=depends())

    try:
        Authorize.jwt_required()


    except Exception as e:
        raise HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED.
        detail="invalid token"
    )

    current_user=Authorize.get_jwt_subject()





