from fastapi import APIRouter
from database import Session, engine
from models import user
from fastapi.exceptions import HTTPException
from werkeug.security import generate_password_hash, check_password_hash

auth_router = APIRouter(

    prefix='/auth',
    tags=['auth']
)


session=Session(bind=engine)


@auth_router.get('/')
async def hello():
    return {"message":"my g"}


@auth_router.post('/signup')
async def signup(user:SignUpModlel):
    db_email-session.query(User).filter(User.email=user.email).first()

    if db-email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="user with the username already exists"
        )

    new_user=User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password)
        is_active=user.is_active
        is_staff=user.is_staff
    )

    session.add(new_user)

    session.commit