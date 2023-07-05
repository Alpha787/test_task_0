from fastapi import APIRouter
from schemas.schemas import NewsSchema
from models.models import NewsModel
from db.BaseEngine import base, engine, sessionLocal

router = APIRouter(
    prefix="/api"
)
       
@router.post("/news/{id}")
async def create_post(news: NewsSchema):
    return "We created a post {id}"
@router.get("/news/{id}")
async def get_post_info(news: NewsSchema):
    return "We get a post {id}"
@router.put("/news/{id}")
async def update_post(news: NewsSchema):
    return "We updated a post {id}"
@router.delete("/news/{id}")
async def delete_post(news: NewsSchema):
    return "We deleted a post {id}"
    
