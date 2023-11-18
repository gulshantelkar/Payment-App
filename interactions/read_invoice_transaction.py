from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
from models.invoice_transaction import InvoiceTransaction
from decimal import Decimal


def read_invoice_transaction(transaction_id,current_user):
    if not current_user:
        raise HTTPException(
            status_code=401, detail="Not authenticated or invalid token"
        )

    admin_role = UserRole.get_or_none((UserRole.user_id == current_user.id) & (UserRole.role == "admin"))
    if not admin_role:
        raise HTTPException(status_code=403, detail="Permission denied. User must have admin role.")

    try:
        transaction = InvoiceTransaction.get(InvoiceTransaction.id == transaction_id)
        transaction_dict = model_to_dict(transaction, exclude=[User.password_hash])
        return transaction_dict
    
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice transaction not found")