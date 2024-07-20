from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext


SECRET_KEY = "082a44f4de695a3d91861ac7ec54cb0dfb5b352a20a26d2d8b2bd6bea63087ab"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def encode_auth_token(email : str):
    payload = {
        'sub': email,
        'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_auth_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload['sub'] 
    except jwt.DecodeError:
        return None

        
        
        
