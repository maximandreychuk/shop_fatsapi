from fastapi import APIRouter, Body
from users import crud
from users.schemas import CreateUser

users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.post('')
# def get_item(email: EmailStr = Body()):   Body - передача параметра в теле запроса
def get_item(user: CreateUser):  # то же самое, только в JSON
    return crud.create_user(user_in=user)
