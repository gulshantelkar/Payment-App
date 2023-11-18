from datetime import  timedelta
import datetime
from fastapi import HTTPException, Depends,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models.user import User
from models.authtoken import AuthToken
import datetime
from params import *

import uuid

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    to_encode["sub"] = str(to_encode["sub"])

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    AuthToken.create(user=uuid.UUID(to_encode["sub"]), token=encoded_jwt, expiration_date=expire)

    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = User.get_or_none(User.id == user_id)
    if user is None:
        raise credentials_exception

    auth_token = AuthToken.get_or_none((AuthToken.user == user.id) & (AuthToken.token == token))
    if not auth_token:
        raise credentials_exception

    return user
