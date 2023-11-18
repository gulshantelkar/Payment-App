from models.user import User
from fastapi import HTTPException
from passlib.hash import bcrypt
from playhouse.shortcuts import model_to_dict


def create_user(user_data):
    existing_user = User.get_or_none((User.username == user_data.username) | (User.email == user_data.email))
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    hashed_password = bcrypt.hash(user_data.password)
    user = User.create(
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_password,
    )
    return model_to_dict(user, exclude=[User.password_hash])