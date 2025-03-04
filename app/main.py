from fastapi import FastAPI
from app.routes import users, product,orders
app = FastAPI()

app.include_router(users.router)
app.include_router(product.router)
app.include_router(orders.router)

@app.get("/")
def read_root():
    return {"detials": "Welcome to root of fulfillx"}