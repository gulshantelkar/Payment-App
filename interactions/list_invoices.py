from models.user_role import UserRole
from fastapi import HTTPException
from models.invoice import Invoice

def list_invoices(current_user):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated or invalid token")

    admin_role = UserRole.get_or_none(
        (UserRole.user_id == str(current_user.id)) & (UserRole.role == "admin")
    )
    if not admin_role:
        raise HTTPException(
            status_code=403, detail="Permission denied. User must have admin role."
        )
    
    invoices = Invoice.select()

    invoices_list = [
        {
            "id": str(invoice.id),
            "amount": float(invoice.amount),
            "description": invoice.description,
            "receiver": {
                "id": str(invoice.receiver.id),
                "username": invoice.receiver.username,
                "email": invoice.receiver.email,
            },
            "payer": {
                "id": str(invoice.payer.id),
                "username": invoice.payer.username,
                "email": invoice.payer.email,
            },
            "status": invoice.status,
            "amount_recovered":invoice.amount_recovered
        }
        for invoice in invoices
    ]

    return invoices_list