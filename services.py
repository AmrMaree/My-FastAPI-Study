from sqlalchemy.orm import Session
import data_access

def get_messages():
    return data_access.get_messages()