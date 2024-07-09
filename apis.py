from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import posts_svc as p_svc

app = FastAPI(title="My FastAPI Project",description="This is my Project's API's Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/",tags=["default"])
def root():
    return {"message": "Welcome to FastAPI"}


@app.get("/messages",tags=["messages"])
def get_messages():
    try:
        message = p_svc.get_messages()
    except Exception as ex:
        return JSONResponse(status_code= 404,content= "No message found")
    return JSONResponse(status_code= 200 ,content= message)

@app.post("/posts",tags=["posts"])
def create_post(title : str, content : str, userid : int):
    result = p_svc.create_post(title, content, userid)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@app.post("/posts/{id}/comments",tags=["posts"])
def create_comment(content : str, post_id: int, user_id : int):
    result = p_svc.create_comment(content, post_id ,user_id)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@app.get("/posts/{id}/comments",tags=["posts"])
def get_post_comments(post_id : int):
    comments = p_svc.get_post_comments(post_id)
    print(comments)
    if comments:
        return {"message": comments}
    return {"message": "No comments found"}

@app.delete("/comments/{comment_id}",tags=["posts"])
def delete_comment(id : int):
    result = p_svc.delete_comment(id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

@app.delete("/posts/{post_id}",tags=["posts"])
def delete_post(id : int):
    result = p_svc.delete_post(id)
    if result["success"]: 
        return JSONResponse(status_code=200,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)