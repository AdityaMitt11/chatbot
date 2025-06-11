from fastapi import APIRouter
from app.models.discount import Discount
from app.database import discount_collection
from bson import ObjectId

router=APIRouter(prefix="/discount",tags=["Discount"])
@router.get("/")
async def get_discount():
    discount=[]
    cursor=discount_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        discount.append(doc)
    return discount

@router.post("/")
async def create_discount(discount:Discount):
    result=await discount_collection.insert_one(discount.model_dump())
    return f"New Discount added with discount id {str(result.inserted_id)}"