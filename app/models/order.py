from pydantic import BaseModel
class Order(BaseModel):
    order_id:str
    user_id:str
    total:float
    status:str