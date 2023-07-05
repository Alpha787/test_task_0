# модели, которые используются в БД
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
# from db.BaseEngine import base
from sqlalchemy.ext.declarative import declarative_base

from pydantic import (
    BaseModel, 
    validator,
)

Base = declarative_base()

class NewsModel(Base):
    __tablename__ = 'News'
    __allow_unmapped__ = True
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    _views = Column(Integer)
    _time_created = Column(DateTime(timezone=True), server_default=func.now())
    
class UsersModel(Base):
    __tablename__ = 'Users'
    __allow_unmapped__ = True
     
       
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    post_num = Column(Integer)
    
     