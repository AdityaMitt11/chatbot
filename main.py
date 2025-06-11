from fastapi import FastAPI
from pydantic import BaseModel
from app.agent.ai_agent import agent_executor
from app.routes import admins
from app.routes import books
from app.routes import discounts
from app.routes import giftvouchers
from app.routes import orders
from app.routes import payments
from app.routes import productcategories
from app.routes import productinventories
from app.routes import reviews
from app.routes import shippings
from app.routes import users
app=FastAPI()
class QueryInput(BaseModel):
    query:str
app.include_router(admins.router)
app.include_router(books.router)
app.include_router(discounts.router)
app.include_router(giftvouchers.router)
app.include_router(orders.router)
app.include_router(payments.router)
app.include_router(productcategories.router)
app.include_router(productinventories.router)
app.include_router(reviews.router)
app.include_router(shippings.router)
app.include_router(users.router)
@app.post("/query")
async def process_query(request: QueryInput):
    user_input = request.query
    result = await agent_executor.ainvoke({"input": user_input})
    return {"response": result["output"]}
@app.get("/")
def root():
    return {"message":"MongoDB-FastAPI Integration"}
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)