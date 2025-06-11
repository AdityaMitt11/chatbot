from fastapi import APIRouter
from app.models.payment import Payment
from app.database import payment_collection
from bson import ObjectId

router=APIRouter(prefix="/payment",tags=["Payment"])
@router.get("/")
async def get_payment():
    payment=[]
    cursor=payment_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        payment.append(doc)
    return payment

@router.post("/")
async def create_payment(payment:Payment):
    result=await payment_collection.insert_one(payment.model_dump())
    return f"New payment added with payment id {str(result.inserted_id)}"