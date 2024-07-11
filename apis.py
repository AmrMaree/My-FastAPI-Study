from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from dac.dac_posts_sqlite import dac_posts_sqlite
from dac.dac_posts_mysql import dac_posts_mysql
from dac.dac_posts_pg import dac_posts_pg
from dac.dac_posts_interface import dac_posts_interface
import posts_svc as p_svc

app = FastAPI(title="My FastAPI Project",description="This is my Project's API's Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
) 

dac_posts :dac_posts_interface  = dac_posts_pg()
my_posts_svc = p_svc.posts_svc(dac_posts)


@app.get("/",tags=["default"])
def root():
    return {"message": "Welcome to FastAPI"}


@app.get("/messages",tags=["messages"])
def get_messages():
    try:
        message = my_posts_svc.get_messages()
    except Exception as ex:
        return JSONResponse(status_code= 404,content= "No message found")
    return JSONResponse(status_code= 200 ,content= message)

@app.post("/posts",tags=["posts"])
def create_post(title : str, content : str, userid : int):
    result = my_posts_svc.create_post(title, content, userid)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@app.post("/posts/{id}/comments",tags=["posts"])
def create_comment(content : str, post_id: int, user_id : int):
    result = my_posts_svc.create_comment(content, post_id ,user_id)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@app.get("/posts/{id}/comments",tags=["posts"])
def get_post_comments(post_id : int):
    comments = my_posts_svc.get_post_comments(post_id)
    print(comments)
    if comments:
        return {"message": comments}
    return {"message": "No comments found"}

@app.delete("/comments/{comment_id}",tags=["posts"])
def delete_comment(id : int):
    result = my_posts_svc.delete_comment(id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@app.delete("/posts/{post_id}",tags=["posts"])
def delete_post(id : int):
    result = my_posts_svc.delete_post(id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@app.get("/posts",tags=["posts"])
def get_posts():
    try:
        post = my_posts_svc.get_posts()
    except Exception as ex:
        return JSONResponse(status_code=404,content="No post found")
    return JSONResponse(status_code=200,content= post)
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)