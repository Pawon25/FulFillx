from sqlalchemy import Column, String, Integer, DECIMAL, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    email = Column(String(100), primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    
class Product(Base):
    __tablename__ = "products"
    name = Column(String(100), primary_key=True, nullable=False)
    description = Column(String(255))
    price = Column(String(255), nullable=False)
    
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String(100), ForeignKey("users.email", ondelete="CASCADE"), nullable=False)
    product_name = Column(String(100), ForeignKey("products.name", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(DECIMAL(10,2), nullable=False)
    status = Column(Enum("pending", "shipped", "delivered", "cancelled"), default="pending")
    order_date = Column(TIMESTAMP, server_default=func.current_timestamp())