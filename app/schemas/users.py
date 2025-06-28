from pydantic import BaseModel


class UserXPResponse(BaseModel):
    name: str
    xp: int
