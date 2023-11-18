from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from peewee import DoesNotExist
from models.invoice import Invoice

def delete_invoice(invoice_id,current_user):
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
        invoice.delete_instance()
        return {"message": "Invoice deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Invoice not found")
    