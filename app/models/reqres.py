from utils.base_session import BaseSession
from config import Server
from http import HTTPStatus


class User:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})
        self._email = kwargs.pop("email", None)
        self._first_name = kwargs.pop("first_name", None)
        self._last_name = kwargs.pop("last_name", None)
        self._avatar = kwargs.pop("avatar", None)
        self._json = json_ if json_ else {
            "email": self._email,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "avatar": self._avatar,
        }

    @property
    def email(self):
        return self._json["email"]

    @property
    def first_name(self):
        return self._json["first_name"]

    @property
    def last_name(self):
        return self._json["last_name"]

    @property
    def avatar(self):
        return self._json["avatar"]


class ResponseUser:
    def __init__(self, **kwargs):
        json_ = kwargs.pop("json", {})
        self._id = kwargs.pop("id", None)
        self._email = kwargs.pop("email", "janet.weaver@reqres.in")
        self._first_name = kwargs.pop("first_name", "Janet")
        self._last_name = kwargs.pop("last_name", "Weaver")
        self._avatar = kwargs.pop("avatar", "https://reqres.in/img/faces/2-image.jpg")
        self._json = json_ if json_ else {
            "first_name": self._first_name,
            "id": self._id,
            "email": self._email,
            "last_name": self._last_name,
            "avatar": self._avatar,
        }

    @property
    def json(self):
        return self._json


class ResponseGetUser:
    def __init__(self, **kwargs):
        response = kwargs.pop("response", None)
        json_ = kwargs.pop("json", response.json() if response else None)
        self._data = kwargs.pop("data", ResponseUser()).json
        self._json = json_ if json_ else self._data,

    @property
    def json(self):
        return self._json


class Reqres:
    def __init__(self, env):
        self.session = BaseSession(base_url=Server(env).reqres)

    def get_user(self, user_id: int):
        response = self.session.get(f"/api/users/{user_id}")
        assert response.status_code == HTTPStatus.OK
        return ResponseGetUser(response=response).json

    def get_user_for_test(self, user_id: int):
        return self.session.get(f"/api/users/{user_id}")

    def get_users(self):
        return self.session.get("/api/users/")

    def get_users_for_pagination(self, data: dict):
        return self.session.get("/api/users/", params=data)

    def greate_user(self, user: dict):
        return self.session.post("/api/users/", json=user)

    def update_user(self, user_id: int, data: dict):
        return self.session.patch(f"/api/users/{user_id}", json=data)

    def delete_user(self, user_id: int):
        return self.session.delete(f"/api/users/{user_id}")

    def greate_user_wrong_method(self, user: dict):
        return self.session.patch("/api/users/", json=user)

    def get_status(self):
        return self.session.get("/status")
