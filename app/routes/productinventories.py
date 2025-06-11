from fastapi import APIRouter
from app.models.productinventory import ProductInventory
from app.database import productinventory_collection
from bson import ObjectId

router=APIRouter(prefix="/productinventory",tags=["ProductInventory"])
@router.get("/")
async def get_productinventory():
    productinventory=[]
    cursor=productinventory_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        productinventory.append(doc)
    return productinventory

@router.post("/")
async def create_productinventory(productinventory:ProductInventory):
    result=await productinventory_collection.insert_one(productinventory.model_dump())
    return f"New productinventory added with product id {str(result.inserted_id)}"