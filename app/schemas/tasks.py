from pydantic import BaseModel


class TaskXPValueResponse(BaseModel):
    xp: int
