from pydantic import BaseModel
class User(BaseModel):
    User_id:str
    name:str
    email:str
    phone:str