from typing import Optional
from fastapi import FastAPI as app
from pydantic import BaseModel
from datetime import datetime


class News(BaseModel):
    description: str
    views: int
    post_date: Optional[datetime] = None
        
    @app.get()
    def get_news():
        return 0
    @app.get()
    def get_description():
        return 0

    @app.get()
    def get_views():
        return 0

    @app.get()
    def get_post_date():
        return 0
    
    @app.post()
    def public_post():
        return
    
    @app.put()
    def update_post():
        return 
