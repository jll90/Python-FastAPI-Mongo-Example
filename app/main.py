from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .db.mongodb_utils import close_mongo_connection, connect_to_mongo
from pydantic import BaseModel
from .db.mongodb import AsyncIOMotorClient, get_database

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class Event(BaseModel):
    user_id: str
    account_id: str

app = FastAPI()


# if not ALLOWED_HOSTS:
#     ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/events")
async def index():
    return [{"event": 1}]


@app.post("/events")
async def create():
    client = await get_database()
    result = await client.test.events.insert_one({"event": 1000})
    return {"message": "success"}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# def on_start():
#     say_something("on_start")

# def on_shutdown():
#     say_something("on_shutdown")

# def say_something(something): 
#     print(something)

# app.add_event_handler("startup", on_start)
# app.add_event_handler("shutdown", on_shutdown)
