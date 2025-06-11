from fastapi import APIRouter
from app.models.review import Review
from app.database import review_collection
from bson import ObjectId

router=APIRouter(prefix="/review",tags=["Review"])
@router.get("/")
async def get_review():
    review=[]
    cursor=review_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        review.append(doc)
    return review

@router.post("/")
async def create_review(review:Review):
    result=await review_collection.insert_one(review.model_dump())
    return f"New review added with review id {str(result.inserted_id)}"