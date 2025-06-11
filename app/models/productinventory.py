from pydantic import BaseModel
class ProductInventory(BaseModel):
    product_id:str
    stock:float
    location:str