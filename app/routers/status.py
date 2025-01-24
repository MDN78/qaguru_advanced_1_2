from http import HTTPStatus
from fastapi import APIRouter
from app.models.AppStatus import AppStatus

# from app.database import users_db


router = APIRouter()


# app status servers
@router.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    return AppStatus(database=True)
