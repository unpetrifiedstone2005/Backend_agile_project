from pydantic import BaseModel

class AddRoleRequest(BaseModel):
    role_id: int

class RemoveRoleRequest(BaseModel):
    role_id: int
