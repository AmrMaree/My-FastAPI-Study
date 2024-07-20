import hashlib
import os

class utils:
    def __init__(self):
        pass

    @staticmethod
    def hash_password_sign_up(password : str):
        salt = os.urandom(16)
        hash_object = hashlib.sha256()
        hash_object.update(salt + password.encode('utf-8'))
        hashed_password = hash_object.hexdigest()
        return hashed_password, salt.hex()
    
    @staticmethod
    def hash_password_login(password : str, salt) -> str:
        hash_object = hashlib.sha256()
        hash_object.update(salt + password.encode('utf-8'))
        hashed_password = hash_object.hexdigest()
        return hashed_password