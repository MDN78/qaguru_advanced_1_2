from pydantic import BaseModel


class AppStatus(BaseModel):
    # flag  -> base with users was downloaded
    users: bool
