import httpx
from app.core.config import settings
from typing import Optional

async def get_external_birth_date() -> Optional[str]:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(settings.EXTERNAL_API_URL, timeout=5.0)
            response.raise_for_status()
            data = response.json()
            return data.get("birthDate")
            
        except (httpx.HTTPStatusError, httpx.RequestError, KeyError) as e:
            print(f"External API error: {e}")
            return None