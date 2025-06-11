from fastapi import APIRouter
from app.models.book import Book
from app.database import book_collection
from bson import ObjectId

router=APIRouter(prefix="/book",tags=["Book"])
@router.get("/")
async def get_books():
    book=[]
    cursor=book_collection.find().limit(5)
    async for doc in cursor:
        doc["_id"]=str(doc["_id"])
        book.append(doc)
    return book

@router.post("/")
async def create_book(book:Book):
    result=await book_collection.insert_one(book.model_dump())
    return f"Book Created with book id {str(result.inserted_id)}"