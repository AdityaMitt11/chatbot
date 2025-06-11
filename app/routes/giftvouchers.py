from fastapi import APIRouter
from app.models.giftvoucher import GiftVoucher
from app.database import giftvoucher_collection
from bson import ObjectId

router=APIRouter(prefix="/giftvoucher",tags=["GiftVoucher"])
@router.get("/")
async def get_giftvoucher():
    giftvoucher=[]
    cursor=giftvoucher_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        giftvoucher.append(doc)
    return giftvoucher

@router.post("/")
async def create_giftvoucher(giftvoucher:GiftVoucher):
    result=await giftvoucher_collection.insert_one(giftvoucher.model_dump())
    return f"New giftvoucher added with voucher id {str(result.inserted_id)}"