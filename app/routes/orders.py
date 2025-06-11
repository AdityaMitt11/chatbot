from fastapi import APIRouter
from app.models.order import Order
from app.database import order_collection
from bson import ObjectId

router=APIRouter(prefix="/orders",tags=["Orders"])
@router.get("/")
async def get_orders():
    order=[]
    cursor=order_collection.find({"status":"shipped"})
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        order.append(doc)
    return order

@router.post("/")
async def create_order(order:Order):
    result=await order_collection.insert_one(order.model_dump())
    return {"message":"order created","order_id":str(result.inserted_id)}