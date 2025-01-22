from pydantic import BaseModel, EmailStr, HttpUrl


class AppStatus(BaseModel):
    # flag  -> base with users was downloaded
    users: bool
