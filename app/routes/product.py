from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.crud import create_product, get_products
from app.schemas import ProductCreate

router = APIRouter(tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products/")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/products/")
def read_products(db: Session = Depends(get_db)):
    return get_products(db)