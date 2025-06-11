from fastapi import APIRouter
from app.models.user import User
from app.database import user_collection
from bson import ObjectId

router=APIRouter(prefix="/user",tags=["User"])
@router.get("/")
async def get_user():
    user=[]
    cursor=user_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        user.append(doc)
    return user

@router.post("/")
async def create_user(user:User):
    result=await user_collection.insert_one(user.model_dump())
    return f"New user added with user id {str(result.inserted_id)}"