from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id :Optional[int]
    username :str
    email:str
    password :str
    is_staff :Optional[bool]
    is_active :Optional[bool]

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                'username':'hoje',
                'email':'biggiemereawoq@gmail.com',
                'password':'password',
                'is_staff':False,
                'is_active':True


            }
        }



 class Settings(BaseModel):
    auth_jwt_secret_key:str='22f8a1c2b7b92240b05d6416ab40e963e0e931ffbc26c9e848a6054191773f6e'

class LoginModel(BaseModel):
    username:str
    password:str
