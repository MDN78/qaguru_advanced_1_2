import json
import uvicorn
from http import HTTPStatus
from fastapi import FastAPI
from models.User import User

app = FastAPI()

# load file to memory
users: list[User]


@app.get("api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id) -> User:
    return users[user_id - 1]


@app.get("api/users/", status_code=HTTPStatus.OK)
def get_users() -> list[User]:
    return users


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
