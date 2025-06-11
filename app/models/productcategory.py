from pydantic import BaseModel
class ProductCategory(BaseModel):
    category_id:str
    name:str