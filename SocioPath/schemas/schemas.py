from datetime import datetime
from typing import Optional
from pydantic import (
    BaseModel, 
    validator,
)

class NewsSchema(BaseModel):
    id: str
    description: Optional[str] | None = None
    _views: int | None = None
    _post_date: Optional[datetime] = None
    
    class Config:
        orm_mode = True
    
class UsersSchema(BaseModel):
    id: int | None = None
    username: str
    post_num: int | None = None
    
    class Config:
        orm_mode = True
    
    # Проверка username на содержание букв
    @validator('username')
    def username_alphanumerc(cls, username: str):
        assert username.isalnum(), 'must be alphanumeric'
        return username
    