from pydantic import BaseModel
class Discount(BaseModel):
    discount_id:str
    code:str
    percentage:float