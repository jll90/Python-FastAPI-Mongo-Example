from ..db.mongodb import AsyncIOMotorClient

async def create_event(conn: AsyncIOMotorClient, data: Any):
    await conn["test"]["events"].insert_one({"event": 123})
    return true
