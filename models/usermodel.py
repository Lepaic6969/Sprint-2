from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    email:str
    name: str
    last_name: str
    documents : dict