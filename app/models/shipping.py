from pydantic import BaseModel
class Shipping(BaseModel):
    shipping_id:str
    order_id:str
    status:str
    carrier:str