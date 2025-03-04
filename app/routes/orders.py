from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.crud import create_order, get_orders, get_orders_by_user
from app.schemas import OrderCreate

router = APIRouter(tags=["Orders"])

@router.post("/orders/")
def add_orders(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_orders(db: Session = Depends(get_db)):
    return get_orders(db)

@router.get("/{user_email}")
def read_orders_by_user(user_email: str, db: Session = Depends(get_db)):
    return get_orders_by_user(db, user_email)