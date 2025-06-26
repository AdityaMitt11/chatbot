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
def format_output(data):
    if isinstance(data, list) and data and isinstance(data[0], dict):
        lines = []
        for idx, item in enumerate(data, 1):
            line = f"{idx}. " + ", ".join(f"{k.replace('_', ' ').title()}: {v}" for k, v in item.items())
            lines.append(line)
        return "\n".join(lines)
    elif isinstance(data, dict):
        return "\n".join(f"{k.replace('_', ' ').title()}: {v}" for k, v in data.items())
    return str(data)
@app.post("/query")
async def process_query(request: QueryInput):
    user_input = request.query
    result = await agent_executor.ainvoke({"input": user_input})
    output = result["output"]
    if isinstance(output, list) and len(output) > 0 and isinstance(output[0], dict):
        keys = list(output[0].keys())
        data = [[item.get(k, "") for k in keys] for item in output]
        if all(isinstance(row[1], (int, float)) for row in data if len(row) > 1):
            return {
                "response": {
                    "type": "chart",
                    "title": "Auto-generated Chart",
                    "labels": [str(row[0]) for row in data],
                    "values": [row[1] for row in data],
                }
            }
        return {
            "response": {
                "type": "table",
                "columns": keys,
                "data": data,
            }
        }
    return {"response": output}
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