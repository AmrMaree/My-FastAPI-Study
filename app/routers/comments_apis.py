from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.dac.dac_posts_sqlite import dac_posts_sqlite
from app.dac.dac_posts_mysql import dac_posts_mysql
from app.dac.dac_posts_pg import dac_posts_pg
from app.dac.dac_posts_interface import dac_posts_interface
import app.services.comments_svc as c_svc

router = APIRouter()

dac_posts :dac_posts_interface  = dac_posts_pg()
my_comments_svc = c_svc.comments_svc(dac_posts)


@router.post("/posts/{id}/comments",tags=["comments"])
def create_comment(content : str, post_id: int, user_id : int):
    result = my_comments_svc.create_comment(content, post_id ,user_id)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])



@router.delete("/comments/{comment_id}",tags=["comments"])
def delete_comment(id : int):
    result = my_comments_svc.delete_comment(id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])


@router.get("/posts/{id}/comments",tags=["comments"])
def get_post_comments(post_id : int):
    comments = my_comments_svc.get_post_comments(post_id)
    print(comments)
    if comments:
        return {"message": comments}
    return {"message": "No comments found"}
