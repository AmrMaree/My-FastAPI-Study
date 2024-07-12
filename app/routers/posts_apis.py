from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dac.dac_posts_sqlite import dac_posts_sqlite
from app.dac.dac_posts_mysql import dac_posts_mysql
from app.dac.dac_posts_pg import dac_posts_pg
from app.dac.dac_posts_interface import dac_posts_interface
import app.services.posts_svc as p_svc

router = APIRouter()

dac_posts :dac_posts_interface  = dac_posts_pg()
my_posts_svc = p_svc.posts_svc(dac_posts)

@router.post("/")
def create_post(title : str, content : str, userid : int):
    result = my_posts_svc.create_post(title, content, userid)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.delete("/{post_id}")
def delete_post(id : int):
    result = my_posts_svc.delete_post(id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@router.get("/")
def get_posts():
    try:
        post = my_posts_svc.get_posts()
    except Exception as ex:
        return JSONResponse(status_code=404,content="No post found")
    return JSONResponse(status_code=200,content= post)
   
