from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
from models.invoice_transaction import InvoiceTransaction


def read_invoice_transactions_by_invoice_id(invoice_id,current_user):
    if not current_user:
        raise HTTPException(
            status_code=401, detail="Not authenticated or invalid token"
        )

    admin_role = UserRole.get_or_none((UserRole.user_id == current_user.id) & (UserRole.role == "admin"))
    if not admin_role:
        raise HTTPException(status_code=403, detail="Permission denied. User must have admin role.")

    try:
        transactions = InvoiceTransaction.select().where(InvoiceTransaction.invoice == invoice_id)
        
        transactions_list = [model_to_dict(transaction, exclude=[User.password_hash]) for transaction in transactions]

        return transactions_list
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice transactions not found for the given invoice id")  