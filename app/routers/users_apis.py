from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dac.dac_posts_sqlite import dac_posts_sqlite
from app.dac.dac_posts_mysql import dac_posts_mysql
from app.dac.dac_posts_pg import dac_posts_pg
from app.dac.dac_posts_interface import dac_posts_interface
import app.services.users_svc as u_svc

router = APIRouter()

dac_posts :dac_posts_interface  = dac_posts_pg()
my_users_svc = u_svc.users_svc(dac_posts)

@router.post("/signup",tags=["users"])
def create_user(name : str, email : str,password : str):
    result = my_users_svc.create_user(name,email,password)
    if result["success"]:
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.post("/login",tags=["users"])
def login(email : str,password : str):
    result = my_users_svc.login(email,password)
    if result["success"]:
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])


@router.get("/",tags=["users"])
def get_users():
    try:
        users= my_users_svc.get_users()
    except Exception as ex:
        return JSONResponse(status_code=404,content="No users found")
    return JSONResponse(status_code=200,content= users)


@router.delete("/")
def delete_user(id : int):
    result = my_users_svc.delete_user(id)
    if result["success"]:
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])