from fastapi import APIRouter
from database import Session, engine

auth_router = APIRouter(

    prefix='/auth',
    tags=['auth']
)


session=Session(bind=engine)


@auth_router.get('/')
async def hello():
    return {"message":"my g"}


@auth_router.post('/signup')
async def signup(user:SignUpModlel)