from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict

def list_users(current_user):
    
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated or invalid token")
    admin_role = UserRole.get_or_none((UserRole.user_id == current_user.id) & (UserRole.role == "admin"))
    if not admin_role:
        raise HTTPException(status_code=403, detail="Permission denied. User must have admin role.")

    users = User.select()
    
    users_list = [model_to_dict(user, exclude=[User.password_hash]) for user in users]
    
    return users_list