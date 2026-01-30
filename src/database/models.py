from dataclasses import dataclass, field
from typing import Optional

@dataclass
class UserProfile:
    user_name: str
    name: str
    skills: list[int] = field(default_factory=list)
    roles: list[int] = field(default_factory=list)
    
@dataclass
class Skill:
    id: int
    skill_name: str

@dataclass
class Role:
    id: int
    role_name: str

@dataclass
class ProfileDraft:
    user_name: Optional[str] = None
    name: Optional[str] = None
    skills: list[int] = field(default_factory=list)
    roles: list[int] = field(default_factory=list)