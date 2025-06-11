from fastapi import APIRouter
from app.models.shipping import Shipping
from app.database import shipping_collection
from bson import ObjectId

router=APIRouter(prefix="/shipping",tags=["Shipping"])
@router.get("/")
async def get_shipping():
    shipping=[]
    cursor=shipping_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        shipping.append(doc)
    return shipping

@router.post("/")
async def create_shipping(shipping:Shipping):
    result=await shipping_collection.insert_one(shipping.model_dump())
    return f"New shipping added with shipping id {str(result.inserted_id)}"