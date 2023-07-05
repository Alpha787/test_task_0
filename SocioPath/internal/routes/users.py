from fastapi import APIRouter
from schemas.schemas import UsersSchema
from models.models import UsersModel
from db.BaseEngine import base, engine, sessionLocal

router = APIRouter(
    prefix='/api'
)
    
@router.get("/")
async def root():
    return {"message":"Hello, World!"}

# исправить здесь ошибку
@router.post('/users/{id}', response_model=UsersSchema)
async def create_user_account(user: UsersSchema):
    db_user = UsersModel(id=user.id,username=user.username, post_num=user.post_num)
    sessionLocal().add(db_user)
    sessionLocal().commit()
    sessionLocal().refresh(db_user)
    return db_user

@router.get("/users/{id}")
async def user_account_info(user: UsersSchema):
    # return JSONResponse({'hello': 'world'})
    return "get user account info"
@router.put("/users/{id}")
async def user_update_info(user: UsersSchema):
    return "update user list with user_id {user.id}"
@router.delete("/users/{id}")
async def user_delete_account(user: UsersSchema):
    return "delete user account"

