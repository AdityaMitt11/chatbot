from fastapi import APIRouter
from app.models.productcategory import ProductCategory
from app.database import productcategory_collection
from bson import ObjectId

router=APIRouter(prefix="/productcategory",tags=["ProductCategory"])
@router.get("/")
async def get_productcategory():
    productcategory=[]
    cursor=productcategory_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        productcategory.append(doc)
    return productcategory

@router.post("/")
async def create_productcategory(productcategory:ProductCategory):
    result=await productcategory_collection.insert_one(productcategory.model_dump())
    return f"New productcategory added with category id {str(result.inserted_id)}"