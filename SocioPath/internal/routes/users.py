from fastapi import APIRouter
from pydantic import ( 
    BaseModel,
    StrictInt,
    ValidationError,
    validator,
)
router = APIRouter(
    prefix='/api'
)

class Users(BaseModel):    
    id: int | None = None
    username: str
    post_num: int | None = None
    
    # Проверка username на содержание букв
    @validator('username')
    def username_alphanumerc(cls, username: str):
        assert username.isalnum(), 'must be alphanumeric'
        return username
    

@router.get("/hello")
async def user_hello():
    return {
        'hello':'world'
    }
    
# Разработать здесь логику API и исправить
    
@router.get("/")
async def root():
    return {"message":"Hello, World!"}

@router.post('/users/{id}')
async def create_user_account(user: Users):
    user = {"user_id": user.id, "username": user.username, "post_num": user.post_num}
    # return JSONResponse(user)
    return "create user account: {user}"

@router.get("/users/{id}")
async def user_account_info(user: Users):
    # return JSONResponse({'hello': 'world'})
    return "get user account info"
@router.put("/users/{id}")
async def user_update_info(user: Users):
    return "update user list with user_id {user.id}"
@router.delete("/users/{id}")
async def user_delete_account(user: Users):
    return "delete user account"

