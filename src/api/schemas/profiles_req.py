from pydantic import BaseModel
from typing import List

class ProfileCreateRequest(BaseModel):
    user_name: str
    name: str
    skills: List[int]
    roles: List[int]