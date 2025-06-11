from fastapi import APIRouter
from app.models.admin import Admin
from app.database import admin_collection
from bson import objectid

router=APIRouter(prefix='/admin',tags=["Admin"])

@router.get("/")
async def get_admin():
    admin=[]
    cursor=admin_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        admin.append(doc)
    return admin

@router.post("/")
async def create_admin(admin:Admin):
    result=await admin_collection.insert_one(admin.model_dump())
    return f"Admin created with admin id {str(result.inserted_id)}"