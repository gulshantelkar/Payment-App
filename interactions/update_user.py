from models.user_role import UserRole
from models.user import User
from fastapi import HTTPException
from passlib.hash import bcrypt
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist
import datetime


def update_user(user_id,user_data,current_user):
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated or invalid token")

    admin_role = UserRole.get_or_none((UserRole.user_id == current_user.id) & (UserRole.role == "admin"))
    if not admin_role and str(current_user.id) != user_id:
        raise HTTPException(status_code=403, detail="Permission denied. User must have admin role or update their own profile.")

    try:
        user = User.get(User.id == user_id)
        user.username = user_data.username
        user.email = user_data.email
        user.password_hash = bcrypt.hash(user_data.password)
        user.updated_at = datetime.datetime.now()
        user.save()
        return model_to_dict(user, exclude=[User.password_hash])
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")