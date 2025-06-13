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
    formatted_output = format_output(output)
    return {"response": formatted_output}
# @app.post("/query")
# async def process_query(request: QueryInput):
#     user_input = request.query
#     result = await agent_executor.ainvoke({"input": user_input})
    
#     # This captures ALL intermediate messages & final output
#     final_output = result.get("output", "")
#     intermediate_steps = result.get("intermediate_steps", [])

#     # Build full response history
#     response_parts = []

#     for step in intermediate_steps:
#         # step is a tuple: (tool invocation, tool result)
#         _, tool_result = step
#         if isinstance(tool_result, list) or isinstance(tool_result, dict):
#             response_parts.append(format_output(tool_result))
#         else:
#             response_parts.append(str(tool_result))

#     # Append the final LLM-generated output as well
#     response_parts.append(final_output)

#     # Join everything
#     full_response = "\n\n".join(response_parts)

#     return {"response": full_response}
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