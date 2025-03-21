from fastapi import APIRouter,Depends
from fastapi _jwt_auth import AuthJWT
from models import User,Order
from schemas import orderModel
from fastapi.exceptions import HTTPException
from database import engine, Session


order_router = APIRouter(
    prefix="/orders",
    tags=['orders']
)


session=Session(bind=engine)

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


@order_router.post('/',status_code=status.HTTP_201_CREATED)

async def place _an_order(order:orderModel,Authorize:AuthJWT=depends())

    try:
        Authorize.jwt_required()


    except Exception as e:
        raise HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED.
        detail="invalid token"
    )

    current_user=Authorize.get_jwt_subject()

    user = session.query(User).filter(User.username=current_user).first()


    new_order =Order(
        pizza_size=order.pizza_size,
        quantity=order.quantity
    )

    new_order.user=user

    session.add(new_user)

    session.commit()












