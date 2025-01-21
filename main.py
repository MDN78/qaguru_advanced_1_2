import uvicorn
from fastapi import FastAPI
from http import HTTPStatus

app = FastAPI()

@app.get("api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id):
    pass

@app.get("api/users/", status_code=HTTPStatus.OK)
def get_users():
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
