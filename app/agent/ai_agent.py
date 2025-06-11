from langchain.agents import create_openai_functions_agent, AgentExecutor
from langgraph.prebuilt import ToolNode
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from app.agent.tools import (
    get_orders, get_users, get_books, get_admins, get_discounts,
    get_reviews, get_giftvouchers, get_categories, get_inventory,
    get_shipping, get_payments
)
tools = [
    get_orders, get_users, get_books, get_admins,
    get_discounts, get_reviews, get_giftvouchers,
    get_categories, get_inventory, get_shipping, get_payments
]
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an intelligent assistant that queries a MongoDB database based on user input."),
    ("user", "{input}"),
    ("assistant", "{agent_scratchpad}")
])
load_dotenv()
llm = ChatOpenAI(model="gpt-4", temperature=0)
agent = create_openai_functions_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True
)