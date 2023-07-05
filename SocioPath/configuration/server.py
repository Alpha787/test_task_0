from fastapi import FastAPI
from SocioPath.configuration.routes import __routes__

class Server:
    __app: FastAPI(title="SocioAPP")
    
    def __init__(self, app: FastAPI) -> None:
        self.__app = app
        self.__register_routes(app)
        
    def get_app(self) -> FastAPI:
        return self.__app
    
    @staticmethod
    def __register_event(app: FastAPI):
        ...
    @staticmethod
    def __register_routes(app: FastAPI):
        __routes__.register_routes(app)
        