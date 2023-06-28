from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class StartUpApp:
    def __init__(self) -> None:
        self.app = FastAPI()
        self.config_routes()
        self.config_middlewares()
        self.config_db()
        
    def config_routes(self):
        return 0
    
    def config_middlewares(self):
        return 0
    
    def config_db(self):
        return 0

if __name__ == '__main__':
    StartUpApp
   
     