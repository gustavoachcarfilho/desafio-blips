from fastapi import APIRouter, HTTPException, Depends
from app.models.lead import LeadCreate, LeadPublic
from app.repositories.lead_repository import LeadRepository
from app.services.external_api import get_external_birth_date
from app.core.database import get_database
from typing import List

router = APIRouter(prefix="/leads", tags=["Leads"])

async def get_repository():
    db = get_database()
    return LeadRepository(db["leads"])

@router.post("/", response_model=LeadPublic, status_code=201)
async def create_lead(
    lead_in: LeadCreate, 
    repo: LeadRepository = Depends(get_repository)
):
    """Creates a new lead with external birth_date integration."""
    birth_date = await get_external_birth_date()
    lead_dict = lead_in.model_dump()
    lead_dict["birth_date"] = birth_date
    return await repo.create(lead_dict)

@router.get("/", response_model=List[LeadPublic])
async def list_leads(repo: LeadRepository = Depends(get_repository)):
    """Returns a list of all leads."""
    return await repo.list_all()

@router.get("/{id}", response_model=LeadPublic)
async def get_lead(id: str, repo: LeadRepository = Depends(get_repository)):
    """Returns a specific lead by ID."""
    lead = await repo.get_by_id(id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead