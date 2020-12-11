from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    password: str

class UserLookUp(BaseModel):
    email: str
    name: str
    last_name: str
    department: str