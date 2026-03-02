from fastapi import FastAPI
from app.api.v1.leads import router as leads_router

app = FastAPI(
    title="Lead Management API",
    description="Refactored API using APIRouter (Controller pattern)",
    version="1.0.0"
)

app.include_router(leads_router)

@app.get("/", tags=["Health"])
async def health_check():
    return {"status": "alive", "service": "lead-management"}