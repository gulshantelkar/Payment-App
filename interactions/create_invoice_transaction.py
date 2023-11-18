from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
from models.invoice import Invoice
from models.invoice_transaction import InvoiceTransaction
from decimal import Decimal

def create_invoice_transaction(transaction_data,current_user):
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
        invoice = Invoice.get(Invoice.id == transaction_data.invoice_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice not found")

    transaction = InvoiceTransaction.create(
        invoice=invoice,
        amount=transaction_data.amount,
        payment_date=transaction_data.payment_date,
        payment_mode=transaction_data.payment_mode,
    )


    invoice.amount_recovered += Decimal(str(transaction_data.amount))
    invoice.save()


    if invoice.amount_recovered >= invoice.amount:
        invoice.status = "completed"
        invoice.save()

    transaction_dict = model_to_dict(transaction, exclude=[User.password_hash])

    return transaction_dict