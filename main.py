import json
import uvicorn
from http import HTTPStatus
from models.User import User
from models.AppStatus import AppStatus
from fastapi import FastAPI, HTTPException
from fastapi_pagination import Page, paginate, add_pagination



app = FastAPI()
add_pagination(app)  # important! add pagination to your app


# load file to memory
users: list[User] = []


# app status servers
@app.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    return AppStatus(users=bool(users))


@app.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    if user_id > len(users):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return users[user_id - 1]


@app.get("/api/users/", response_model=Page[User])
def get_users() -> Page[User]:
    return paginate(users)


if __name__ == "__main__":
    # read file from memory
    with open("users.json") as f:
        users = json.load(f)
    # validation dates in file
    for user in users:
        User.model_validate(user)
    print("Users loaded")
    # start server
    uvicorn.run(app, host="localhost", port=8002)
