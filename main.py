import datetime
from fastapi import FastAPI
from fastapi import HTTPException

from db.userdb import UserInDB
from db.userdb import database_users
from db.userdb import update_user, get_user
from models.usermodel import UserIn, UserOut, UserAuth

##########################################################################################
from fastapi.middleware.cors import CORSMiddleware
origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080","http://localhost:8081","https://dokimanapp.herokuapp.com",
]
api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


##########################################################################################

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

@api.get("/user/balance/{email}")
async def get_document(email:str):
    user_in_db = get_user(email)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.post("/user/signup/")
async def create_user(new_user: UserInDB):
    new_key = get_user(new_user.email)
    if new_key != None:
        raise HTTPException(status_code=409, detail="Este usuario ya existe")
    database_users[new_key]= new_user
    user_auth = UserAuth(**new_user.dict())
    return {"mensaje": "Usuario creado exitosamente", "usuario": user_auth}
