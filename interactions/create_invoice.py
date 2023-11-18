from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
import uuid
from models.invoice import Invoice


def create_invoice(invoice_data,current_user):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated or invalid token")

    admin_role = UserRole.get_or_none((UserRole.user_id == current_user.id) & (UserRole.role == "admin"))
    if not admin_role:
        raise HTTPException(status_code=403, detail="Permission denied. User must have admin role.")

    try:
        receiver_user = User.get(User.id == uuid.UUID(invoice_data.receiver))
        payer_user = User.get(User.id == uuid.UUID(invoice_data.payer))
    except DoesNotExist:
        raise HTTPException(status_code=400, detail="Receiver or payer not found in the database")

    invoice = Invoice.create(
        amount=invoice_data.amount,
        description=invoice_data.description,
        receiver=receiver_user,
        payer=payer_user,
        status=invoice_data.status,
        amount_recovered=invoice_data.amount_recovered
    )

    response = model_to_dict(invoice, exclude=[User.password_hash])
    response['receiver'] = model_to_dict(receiver_user, exclude=[User.password_hash])
    response['payer'] = model_to_dict(payer_user, exclude=[User.password_hash])
    
    return response