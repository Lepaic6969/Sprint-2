import datetime
from fastapi import FastAPI
from fastapi import HTTPException

from db.userdb import UserInDB
from db.userdb import database_users
from db.userdb import update_user, get_user, user_lookup_clearance
from models.usermodel import UserIn, UserLookUp,UserUpdatePassword

api=FastAPI()

@api.post("/user/login/")
async def login(user_in: UserIn):
    user_in_db = get_user(user_in.email)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.get("/users/clearance/{clear}")
async def get_users_by_clearance(clear: int):
    user_in_db = user_lookup_clearance(clear)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserLookUp(**user_in_db.dict())
    return user_out

@api.put("/user/update/")
async def update(user_in:UserUpdatePasword):
    user_in_db=get_user(user_in.email)
    if user_in_db==None:
        raise HTTPException(status_code=404,
                           detail="El usuariono existe")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=400,
                            detail="La clave del usuario es incorrecta")
    
    user_in_db.password=user_in.new_password
    n=update_user(user_in_db)
    return n