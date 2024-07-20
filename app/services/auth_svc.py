from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

SECRET_KEY = "082a44f4de695a3d91861ac7ec54cb0dfb5b352a20a26d2d8b2bd6bea63087ab"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

class Token(BaseModel):
    access_token : str
    token_type : str

class DataToken(BaseModel):
    id: Optional[str] = None 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token : str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM)
        id :str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = DataToken(id=id)
    except jwt.ExpiredSignatureError:
        raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = verify_access_token(token, credentials_exception)
        
        
        
