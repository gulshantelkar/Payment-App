from pydantic import BaseModel
import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserUpdate(BaseModel):
    username: str
    email: str
    password: str


class InvoiceCreate(BaseModel):
    amount: float
    description: str
    receiver:str
    payer:str
    status:str='pending'
    amount_recovered:float=0


class InvoiceTransactionCreate(BaseModel):
    invoice_id: str
    amount: float
    payment_date: datetime.datetime
    payment_mode: str
