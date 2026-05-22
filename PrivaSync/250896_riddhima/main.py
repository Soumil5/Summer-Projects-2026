from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Header
from fastapi import FastAPI, Cookie


fastapi = FastAPI()
class Item(BaseModel):
    name: str
    price: float
@fastapi.post("/items")
async def create_item(item: Item):
    return {"item": item}
@fastapi.get("/items")
async def read_items(user_agent: str = Header(None)):
    return {"User-Agent": user_agent}
@fastapi.get("/items/")
async def read_items(session_token: str = Cookie(None)):
    return {"session_token": session_token}








@fastapi.get("/")
async def home():

    return{"message" : "task api is working"}