import json
import uvicorn
from app.models.User import User
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from routers import status, users
from database import users_db


app = FastAPI()
add_pagination(app)  # important! add pagination to your app
app.include_router(status.router)
app.include_router(users.router)



if __name__ == "__main__":
    # read file from memory
    with open("../users.json") as f:
        users_db.extend(json.load(f))
        print(users_db)

    # validation dates in file
    for user in users_db:
        User.model_validate(user)
    print("Users loaded")
    # start server
    uvicorn.run(app, host="localhost", port=8002)
