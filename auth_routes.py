from fastapi import APIRouter
from database import Session, engine
from models import user
from fastapi.exceptions import HTTPException

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