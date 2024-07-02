from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import services

app = FastAPI(title="My FastAPI Project",description="This is my Project's API's Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins 
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}


@app.get("/messages")
def get_messages():
    message = services.get_messages()
    if message:
        return {"message": message}
    return {"message": "No message found"}

@app.post("/posts")
def create_post(title : str, content : str, userid : int):
    result = services.create_post(title, content, userid)
    if result["success"]: 
        return JSONResponse(status_code=201,content= result["message"])
    return JSONResponse(status_code= 404,content= result["message"])

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)