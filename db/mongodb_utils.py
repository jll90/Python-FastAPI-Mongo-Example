import logging

from motor.motor_asyncio import AsyncIOMotorClient
# from ..core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

MONGODB_URL = "mongodb://localhost:27017"


async def connect_to_mongo():
    logging.info("Connecting to Mongodb...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL))
                                   # maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   # minPoolSize=MIN_CONNECTIONS_COUNT)
    logging.info("Connected to Mongodb...")


async def close_mongo_connection():
    logging.info("Closing connection to Mongodb...")
    db.client.close()
    logging.info("Disconnected from Mongodb...")
