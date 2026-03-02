from motor.motor_asyncio import AsyncIOMotorCollection
from app.models.lead import LeadCreate
from bson import ObjectId
from typing import List, Optional

class LeadRepository:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create(self, lead_data: dict) -> dict:
        result = await self.collection.insert_one(lead_data)
        return await self.collection.find_one({"_id": result.inserted_id})

    async def list_all(self) -> List[dict]:
        return await self.collection.find().to_list(length=None)

    async def get_by_id(self, lead_id: str) -> Optional[dict]:
        if not ObjectId.is_valid(lead_id):
            return None
            
        return await self.collection.find_one({"_id": ObjectId(lead_id)})