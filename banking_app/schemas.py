from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    surname: str
    amount: float


class CustomerIn(CustomerBase):
    login: str
    password: str


class CustomerOut(CustomerBase):
    id: int

    class Config:
        orm_mode = True
