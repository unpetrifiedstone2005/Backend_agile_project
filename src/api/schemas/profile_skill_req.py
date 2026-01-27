from pydantic import BaseModel

class AddSkillRequest(BaseModel):
    skill_id: int

class RemoveSkillRequest(BaseModel):
    skill_id: int
