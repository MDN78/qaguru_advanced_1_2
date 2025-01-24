from typing import Iterable

from sqlmodel import Session, select
from app.database.engine import engine
from app.models.User import User


def get_user(user_id: int) -> User | None:
    with Session(engine) as session:
        return session.get(User, user_id)


def get_users() -> Iterable[User]:
    with Session(engine) as session:
        statement = select(User)
        return session.exec(statement).all()
