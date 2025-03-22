from fastapi import APIRouter,Depends
from fastapi_jwt_auth import AuthJWT
from models import User,Order
from schemas import orderModel, OrderStatausModel
from fastapi.exceptions import HTTPException
from database import engine, Session
from fastapi.encoders import jsonable_encoder


order_router = APIRouter(
    prefix="/orders",
    tags=['orders']
)


session=Session(bind=engine)

@order_router.get('/')
async def hello(Authorize:AuthJWT=Depends()):


    """
    ## a sample hello world route

    this is used to jot down the documentation of this route 
    in swagger ui i can say
    """

    try:
        Authorize.jwt_required()



    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )

    return {"message":"hellow worman"}


@order_router.post('/',status_code=status.HTTP_201_CREATED)
async def place_an_order(order:orderModel,Authorize:AuthJWT=depends()):

    """
    ##placing an order
    this 
    """

    try:
        Authorize.jwt_required()


    except Exception as e:
        raise HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid token"
    )

    current_user=Authorize.get_jwt_subject()

    user = session.query(User).filter(User.username==current_user).first()


    new_order =Order(
        pizza_size=order.pizza_size,
        quantity=order.quantity
    )

    new_order.user=user

    session.add(new_order)

    session.commit()


    response={
        "pizza_size":new_order_size,
        "quantity":new_order.quantity,
        "id":new_order.id,
        "order_status":new_order.order_status
    }

    return jsonable_encoder(response)



@order_router.get('/orders')
async def list_all_orders(Authorize:AuthJWT=Depends()):

    try:
        Authorize.jwt_required()

    except Exception as e :
        raise HTTPException(status_code=status_code.HTTP_401_UNAUTHORIZED,
            detail='invalid token'
        )

    current_user=Authorize.get_jwt_subject()

    user=session.query(User).filter(User.username==current_user).first()

    if user.is_staff:
        orders=session.query(Order).all()

        return jsonable_encoder(orders)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='invalid user'
    )

        


@order_router.get('/orders/{id}')
async def get_order_by_id(id:int,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invthis user is not allowed to this alise "
        )

    user=Authorize.get_jwt_subject()

    current_user=session.query(User).filter(User.username==user)

    if current_user.is_staff:

        order= session.query(Order).filter(Order.id==id).first()

        return jsonable_encoder(order)


    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='user not allowed to carry out the requerst'
    )


@order_router.get('/users/order')
async def get_user_order(Authorize: AuthJWT = Depends(), session: Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"  # ✅ Corrected from 'details' to 'detail'
        )

    user = Authorize.get_jwt_subject()

    current_user = session.query(User).filter(User.username == user).first()
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    session.refresh(current_user)  # ✅ Refresh user if needed
    return jsonable_encoder(current_user.orders)

@order_router.get('/user/order/{order_id}')
async def get_specific_order(id:int,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )

    subject=Authorize.get_jwt_subject()

    current_user=session.query(User).filter(User.username==subject).first()

    orders=current_user.orders

    for o in orders:

        if o.id==id:

            return jsonable_encoder(o)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="nw ordera having such id"
    )


@order_router.put('/order/update/{id}')
async def update_order(id:int,order:orderModel,Authorize:AuthJWT=Depends()):

    try:
        Authorize.jwt_required()

    except:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )

    order_to_update=session.query(Orders).filter(Order.id==id).first()

    order_to_update.quantity=order.quantity

    order_to_update.pizza_size=order.pizza_size

    session.commit()

    return jsonable_encoder(order_to_update)





@order_router.patch("/order/update/{id}")
async def update_order_status(id:int,order:OrderStatausModel,Authorize:Authjwt=Depends()):
    try:
        Authorize.jwt_required()

    except:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )

    username=Authorize.get_jwt_subject()

    current_user=session.query(User).filter(User.username==username)

    if current_user.is_staff:
        order=session.query(Order).filter(Order.id==id).first()

        order_to_update.order_status=order.order_status

        session.commit()

        response={
            "quantity":order_to_update.quantity,
            "pizza_size":order_to_update.pizza_size,
            "order_status":order_to_update.order_status
        }

        return jsonable_encoder(response)



@order_router.delete("/order/delete/{id}")
async def delete_an_order(id:int,Authorize:AuthJWT=Depends()):
     try:
        Authorize.jwt_required()

     except:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )


     order_to_delete=session.query(Order).filter(Order.id==id).first()

     session.delete(order_to_delete)

     session.commit()

     return jsonable_encoder(order_to_delete)

    








