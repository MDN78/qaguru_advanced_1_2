from fastapi import APIRouter, HTTPException
from http import HTTPStatus
from app.models.User import User
from app.main import users
from fastapi_pagination import Page, paginate

router = APIRouter()


@router.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    if user_id > len(users):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return users[user_id - 1]


@router.get("/api/users/", response_model=Page[User])
def get_users() -> Page[User]:
    return paginate(users)
