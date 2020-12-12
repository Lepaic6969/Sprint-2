from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    email: str
    password: str
    name: str
    last_name: str
    department: str
    clearance: int
    
database_users = Dict[str,UserInDB]

database_users = {
    "cinthya@example.com": UserInDB(**{"email": "cinthya@example.com",
                                        "password": "ejemplo123",
                                        "name": "Cinthya",
                                        "last_name":"Murgas",    
                                        "department": "Gerencia",
                                        "clearance" : 5}),
    "martin@example.com" : UserInDB(**{"email": "martin@example.com",
                                        "password": "ejemplo987",
                                        "name": "Martin",
                                        "last_name":"Vasquez",
                                        "department": "Finanzas",
                                        "clearance": 4}),
    "camilo@example.com" : UserInDB(**{"email": "camilo@example.com",
                                        "password": "example345",
                                        "name": "Camilo",
                                        "last_name":"Zamora",    
                                        "department": "Mercadeo",
                                        "clearance": 3}),
    "edwin@example.com" : UserInDB(**{"email": "edwin@example.com",
                                        "password": "example123",
                                        "name": "Edwin",
                                        "last_name":"Gonzalez",    
                                        "department": "Ventas",
                                        "clearance": 2}),
}

def get_user(email:str):
    if email in database_users.keys():
        return database_users[email]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.email] = user_in_db
    return user_in_db

#Autorización de búsqueda de usuario

    
def user_lookup_clearance(clear:str):
    if clear <=5:
        for k in database_users:
            if UserInDB["clearance"] == clear:
                return database_users.values(k)
            
