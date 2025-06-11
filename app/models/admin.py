from pydantic import BaseModel
class Admin(BaseModel):
    admin_id:str
    admin_name:str
    email:str