from pydantic import BaseModel, Field, BeforeValidator
from typing import Optional, Annotated
from datetime import date

PyObjectId = Annotated[str, BeforeValidator(str)]

class LeadBase(BaseModel):
    name: str = Field(..., min_length=1)
    email: str 
    phone: str

class LeadCreate(LeadBase):
    pass

class LeadPublic(LeadBase):
    id: PyObjectId = Field(alias="_id")
    birth_date: Optional[str] = None

    class Config:
        populate_by_name = True