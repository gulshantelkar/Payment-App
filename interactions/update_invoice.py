from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
import datetime

from models.invoice import Invoice

def update_invoice(invoice_id,invoice_data,current_user):
    if not current_user:
        raise HTTPException(
            status_code=401, detail="Not authenticated or invalid token"
        )

    admin_role = UserRole.get_or_none(
        (UserRole.user_id == str(current_user.id)) & (UserRole.role == "admin")
    )
    if not admin_role:
        raise HTTPException(
            status_code=403, detail="Permission denied. User must have admin role."
        )

    try:
        invoice = Invoice.get(Invoice.id == invoice_id)
        invoice.amount = invoice_data.amount
        invoice.description = invoice_data.description
        invoice.receiver = User.get(User.id == invoice_data.receiver)
        invoice.payer = User.get(User.id == invoice_data.payer)
        invoice.status = invoice_data.status
        invoice.amount_recovered=invoice_data.amount_recovered
        invoice.updated_at = datetime.datetime.now()
        invoice.save()
        return model_to_dict(invoice)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice not found")