from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy.orm import Session
from database import engine
from models import User
from werkzeug.security import generate_password_hash
from schemas import SignUpModel,LoginModel
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder

auth_router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

session = Session(bind=engine)


@auth_router.get('/')
async def hello():
    return {"message": "my g"}


@auth_router.post('/signup', 
                  status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):  # Corrected typo here
    db_email = session.query(User).filter(User.email == user.email).first()  # Corrected typo here

    if db_email is not None:
        # Raise HTTPException instead of returning it
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    # Hashing the password using werkzeug
    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),  # Hashing the password
        is_active=user.is_active,
        is_staff=user.is_staff
    )

    session.add(new_user)
    session.commit()

    return new_user


@auth_router.post('/login')
async def login(user:LoginModel,Authorize:Authjwt=Depends()):
    db_user=session.query(User).filter(User.username==user.username).first()

    if db_user and check_password_hash(db_user.password,user.password)
        access_token=Authorize.create_access_token(subject=db_user.username)
        refresh_token=Authorize.create_refresh_t0ken(subject=db_user.username)


        response={
            "access":access_token,
            "refresh":refresh_token

        }

    raise HTTPException(status_code.HTTP_400_BAD_REQUEST,
    detail="invalid user or password")