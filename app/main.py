import json
import uvicorn
from app.models.User import User
from fastapi import FastAPI, HTTPException
from fastapi_pagination import Page, paginate, add_pagination

app = FastAPI()
add_pagination(app)  # important! add pagination to your app

# load file to memory
users: list[User] = []

if __name__ == "__main__":
    # read file from memory
    with open("../users.json") as f:
        users = json.load(f)
    # validation dates in file
    for user in users:
        User.model_validate(user)
    print("Users loaded")
    # start server
    uvicorn.run(app, host="localhost", port=8002)
