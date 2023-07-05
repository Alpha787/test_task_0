# Модель - движок для работы с базой данных
from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql+asyncpg:///sociopath.db", echo=True)
base = declarative_base()
sessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
