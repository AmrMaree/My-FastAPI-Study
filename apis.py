from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
    print("11")
    return {"message": "Welcome to FastAPI"}


@app.get("/messages")
def get_messages():
    message_content = services.get_messages()
    if message_content:
        return {"message": message_content}
    return {"message": "No message found"}



if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)