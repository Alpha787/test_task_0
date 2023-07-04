from fastapi import APIRouter
from typing import Optional
from pydantic import (
    BaseModel,
    StrictInt, 
    ValidationError, 
    validator
)
from datetime import datetime

router = APIRouter(
    prefix="/api"
)

class News(BaseModel):
    id: str
    description: Optional[str] | None = None
    _views: int
    _post_date: Optional[datetime] = None
        
@router.post("/news/{id}")
async def create_post():
    return 0
@router.get("/news/{id}")
async def get_post_info():
    return 0
@router.put("/news/{id}")
async def update_post():
    return 0
@router.delete("/news/{id}")
async def delete_post():
    return 0
    
