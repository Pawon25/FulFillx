from sqlalchemy.orm import Session
from app.models import User, Product, Order
from app.schemas import UserCreate, ProductCreate, OrderCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_order(db: Session, order: OrderCreate):
    product = db.query(Product).filter(Product.name ==order.product_name).first()
    if not product:
        return None
    
    total_price = order.quantity * product.price
    db_order = Order(**order.dict(), total_price=total_price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_users(db: Session):
    return db.query(User).all()

def get_products(db: Session):
    return db.query(Product).all()

def get_orders(db: Session):
    return db.query(Order).all()

def get_orders_by_user(db: Session, user_email: str):
    return db.query(Order).filter(Order.user_email == user_email).all()