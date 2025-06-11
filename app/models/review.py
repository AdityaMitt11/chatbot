from pydantic import BaseModel
class Review(BaseModel):
    review_id:str
    product_id:str
    rating:float
    comment:str