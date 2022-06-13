from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import engine
from .dependencies import get_db
from . import schemas, models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/customers")
def get_customers(min_amount: Optional[int | float] = None,
                  max_amount: Optional[int | float] = None,
                  db: Session = Depends(get_db)):
    return crud.get_customers(db=db,
                              min_amount=min_amount,
                              max_amount=max_amount)


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db=db, customer_id=customer_id)
    if customer:
        return customer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Customer not found")


@app.post("/customers",
          response_model=schemas.CustomerOut,
          status_code=status.HTTP_201_CREATED)
def post_customer(customer: schemas.CustomerIn, db: Session = Depends(get_db)):
    return crud.post_customer(db=db, customer=customer)
