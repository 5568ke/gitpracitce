from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_dict={}


class User(BaseModel):
    student_id : str
    name : str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/register")
def register(user: User):
    user_dict[user.student_id]=user.name
    return {"message" : "register succussfully"}
