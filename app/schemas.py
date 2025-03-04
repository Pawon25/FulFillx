from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float
    
class OrderCreate(BaseModel):
    user_email: str
    product_name: str
    quantity: int

class OrderResponse(OrderCreate):
    id: int
    total_price: float
    status: str
    order_date: datetime