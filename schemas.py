from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'username': 'hoje',
                'email': 'biggiemereawoq@gmail.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '22f8a1c2b7b92240b05d6416ab40e963e0e931ffbc26c9e848a6054191773f6e'


class LoginModel(BaseModel):
    username: str
    password: str


class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = 'PENDING'
    pizza_size: Optional[str] = 'SMALL'
    user_id: Optional[int]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status: Optional[str] = 'PENDING'  # ✅ Fixed Optional[str] usage

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "order_status": "PENDING"
            }
        }
