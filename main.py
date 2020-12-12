import datetime
from fastapi import FastAPI
from fastapi import HTTPException

from db.userdb import UserInDB
from db.userdb import database_users
from db.userdb import update_user, get_user
from models.usermodel import UserIn, UserOut

api = FastAPI()

@api.get("/")
async def home():
    return{"message":"Dokiman: File Management"}

@api.post("/user/login/")
async def login(user_in: UserIn):
    user_in_db = get_user(user_in.email)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.get("/users/documents/{email}")
async def get_document(email:str):
    user_in_db = get_user(email)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out