from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForignKey
from sqlalchemy_utils import ChoiceType


class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(25),unique=True)
    email=Column(String(80),unique=True)
    password=Column(Text,nullable=True)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)


    def __repr__(self):
        return f"<User {self.username}"

class Order (Base):

    ORDER_STATUSES=(
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELEVERED','delivered')
    )
    PIZZA_SIZES=(
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large'),
        ('EXTRA-LARGE','extra-large')
    )
    __tablename__="orders"
    id=Column(Integer,primary_key=True)
    quantity=Column(Integer,nullable=True)
    order_statuses=Column(ChoiceType(Choices=ORDER_STATUSES,default='pending'))
    pizza_size=Column(ChoiceType(Choices=PIZZA_SIZES, default='SMALL'))