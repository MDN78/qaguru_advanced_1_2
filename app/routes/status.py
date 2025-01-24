from fastapi import APIRouter
from http import HTTPStatus
from app.models.AppStatus import AppStatus
from app.main import users


router = APIRouter()


# app status servers
@router.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    return AppStatus(users=bool(users))
