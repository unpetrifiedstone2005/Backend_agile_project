from pydantic import BaseModel
from typing import Optional, List

class ProfileUpdateRequest(BaseModel):
    name: Optional[str] = None
    skills: Optional[List[int]] = None
    roles: Optional[List[int]] = None
