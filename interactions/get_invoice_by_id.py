from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
import datetime
import uuid
from models.invoice import Invoice

def get_invoice_by_id(invoice_id,current_user):
    try:
        invoice = Invoice.get(Invoice.id == invoice_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated or invalid token")

    is_admin = UserRole.get_or_none((UserRole.user_id == current_user.id) & (UserRole.role == "admin"))
    is_receiver = str(invoice.receiver) == str(current_user.id)
    is_payer = str(invoice.payer) == str(current_user.id)


    if not is_admin and not is_receiver and not is_payer:
        raise HTTPException(status_code=403, detail="Permission denied. User must be receiver, payer, or admin.")

    response = model_to_dict(invoice, exclude=[User.password_hash])
    response['receiver'] = model_to_dict(invoice.receiver, exclude=[User.password_hash])
    response['payer'] = model_to_dict(invoice.payer, exclude=[User.password_hash])

    return response