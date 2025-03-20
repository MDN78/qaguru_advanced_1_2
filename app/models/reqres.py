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
        # self._json = json_ if json_ else {
        #     "data": self._data,
        # }

    @property
    def json(self):
        return self._json


# class ResponseListUsers:
#     def __init__(self, **kwargs):
#         json_ = kwargs.pop("json", {})
#
#         self._json = json_ if json_ else {
#             "items": [],
#             "total": 12,
#             "page": 1,
#             "size": 50,
#             "pages": 1,
#         }
#
#     def add_user(self, user: ResponseUser):
#         self._json['items'].append(user.json)
#         return self
#
#     @property
#     def json(self):
#         return self._json
