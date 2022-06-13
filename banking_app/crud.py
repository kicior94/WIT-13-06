from typing import Optional
from sqlalchemy.orm import Session
from . import schemas, models


def get_customers(
        db: Session,
        min_amount: Optional[int | float] = None,
        max_amount: Optional[int | float] = None) -> list[models.Customer]:

    if min_amount and max_amount:
        return db.query(models.Customer).filter(
            models.Customer.amount >= min_amount,
            models.Customer.amount <= max_amount).all()
    elif max_amount:
        return db.query(models.Customer).filter(
            models.Customer.amount <= max_amount).all()
    elif min_amount:
        return db.query(models.Customer).filter(
            models.Customer.amount >= min_amount).all()
    else:
        return db.query(models.Customer).all()


def get_customer(db: Session, customer_id: int) -> models.Customer | None:
    return db.query(
        models.Customer).filter(models.Customer.id == customer_id).first()


def post_customer(db: Session,
                  customer: schemas.CustomerIn) -> models.Customer:
    new_customer = models.Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer
