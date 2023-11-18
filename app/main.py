from fastapi import FastAPI, HTTPException, Depends

from passlib.hash import bcrypt
from peewee import DoesNotExist
from models.user import User
from models.invoice import Invoice
from models.user_role import UserRole
from params import *
from database import database

import uuid
from fastapi.security import OAuth2PasswordRequestForm
from app.__init__ import json_encoder
from fastapi.responses import JSONResponse

from interactions.create_user import create_user
from interactions.read_user import read_user
from interactions.update_user import update_user
from interactions.list_users import list_users
from interactions.create_invoice import create_invoice
from interactions.get_invoice_by_id import get_invoice_by_id
from interactions.list_invoices import list_invoices
from interactions.update_invoice import update_invoice
from interactions.delete_invoice import delete_invoice
from interactions.create_invoice_transaction import create_invoice_transaction
from interactions.read_invoice_transaction import read_invoice_transaction
from interactions.read_invoice_transactions_by_invoice_id import read_invoice_transactions_by_invoice_id


from helper.authentication import *


app = FastAPI()

# with database:
#     database.create_tables([InvoiceTransaction,Invoice,AuthToken,User,UserRole]) 

@app.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User.get_or_none(User.username == form_data.username)
    if user and bcrypt.verify(form_data.password, user.password_hash):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.id}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/users/")
async def create_user_data(user_data: UserCreate):
    try:
        data = create_user(user_data)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })

@app.get("/users/{user_id}")
async def read_user_data(user_id: str, current_user: User = Depends(get_current_user)):
    try:
        data = read_user(user_id,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })



@app.put("/users/{user_id}")
async def update_user_data(user_id: str, user_data: UserUpdate, current_user: User = Depends(get_current_user)):
    try:
        data = update_user(user_id,user_data,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
  


@app.get("/users/")
async def list_users_data(current_user: User = Depends(get_current_user)):
    try:
        data = list_users(current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
   

@app.delete("/users/{user_id}")
async def delete_user(user_id: str, current_user: User = Depends(get_current_user)):
    try:
        if not current_user:
            raise HTTPException(status_code=401, detail="Not authenticated or invalid token")
        user_to_delete = User.get(User.id == user_id)
        admin_role = UserRole.get_or_none((UserRole.user_id == current_user.id) & (UserRole.role == "admin"))
        if not admin_role:
            raise HTTPException(status_code=403, detail="Permission denied. User must have admin role.")

        user_to_delete.delete_instance()
        return {"message": "User deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/invoices/")
async def create_invoice_data(
    invoice_data: InvoiceCreate,
    current_user: User = Depends(get_current_user),
):
    try:
        data = create_invoice(invoice_data,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
    

@app.get("/invoices/{invoice_id}")
async def get_invoice_by_id_data(
    invoice_id: uuid.UUID,
    current_user: User = Depends(get_current_user)
):
    try:
        data = get_invoice_by_id(invoice_id,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
  

@app.get("/invoices/")
async def list_invoices_data(current_user: User = Depends(get_current_user)):
    try:
        data = list_invoices(current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })


@app.put("/invoices/{invoice_id}")
async def update_invoice_data(
    invoice_id: str, invoice_data: InvoiceCreate, current_user: User = Depends(get_current_user)
):
    try:
        data = update_invoice(invoice_id,invoice_data,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
    
 

@app.delete("/invoices/{invoice_id}")
async def delete_invoice_data(
    invoice_id: str, current_user: User = Depends(get_current_user)
):
    try:
        data = delete_invoice(invoice_id,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
    
    
@app.post("/invoice-transactions/")
async def create_invoice_transaction_data(
    transaction_data: InvoiceTransactionCreate, current_user: User = Depends(get_current_user)
):
    try:
        data = create_invoice_transaction(transaction_data,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })


@app.get("/invoice-transactions/{transaction_id}")
async def read_invoice_transaction_data(
    transaction_id: str,
    current_user: User = Depends(get_current_user)
):  
    try:
        data = read_invoice_transaction(transaction_id,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
    
   
    
@app.get("/invoice-transactions/invoice/{invoice_id}")
async def read_invoice_transactions_by_invoice_id_data(
    invoice_id: str,
    current_user: User = Depends(get_current_user)
):  
    try:
        data = read_invoice_transactions_by_invoice_id(invoice_id,current_user)
        return JSONResponse(status_code=200, content=json_encoder(data))
    except HTTPException as e:
        raise
    except Exception as e:
        return JSONResponse(status_code=500, content={ "success": False, 'error': str(e) })
   
    
@app.post("/webhooks/payment/success")
async def handle_payment_success(payload: dict):
    try:
        invoice_id = payload.get("invoice_id")
        amount_paid = payload.get("amount_paid")
        
        invoice = Invoice.get(Invoice.id == invoice_id)
        
        if amount_paid == invoice.amount:
            invoice.status = "completed"
            invoice.save()
            
            return {"status": "success", "message": "Payment successfully processed"}
        else:
            raise HTTPException(status_code=400, detail="Invalid payment amount")
            
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice not found")

    
    
@app.post("/webhooks/payment/failure")
async def handle_payment_failure(payload: dict):
    try:
        invoice_id = payload.get("invoice_id")
        invoice = Invoice.get(Invoice.id == invoice_id)
        
        invoice.status = "payment_failed"
        invoice.save()
  
        return {"status": "success", "message": "Payment failure processed"}
        
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice not found")



@app.post("/webhooks/refund")
async def handle_refund(payload: dict):
    try:
        invoice_id = payload.get("invoice_id")
        refunded_amount = payload.get("refunded_amount")
    
        invoice = Invoice.get(Invoice.id == invoice_id)
        if refunded_amount <= invoice.amount:
            invoice.status = "refunded"
            invoice.save()
            
            return {"status": "success", "message": "Refund processed"}
        else:
            raise HTTPException(status_code=400, detail="Invalid refunded amount")
        
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice not found")