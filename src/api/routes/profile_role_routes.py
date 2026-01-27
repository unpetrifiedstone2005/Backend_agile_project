from fastapi import APIRouter, HTTPException
from src.api.schemas.profile_role_req import AddRoleRequest, RemoveRoleRequest
from src.services.profileRoleServices import ProfileDraftRoleService
from src.database.role_repository import RoleRepository
from src.database.models import UserProfile

router = APIRouter(
    prefix="/profiles/draft/roles",
    tags=["Profile Draft Roles"]
)

# TEMP draft store (replace with your real draft mechanism)
DRAFT_STORE: dict[str, UserProfile] = {}

def get_draft(user_name: str) -> UserProfile:
    if user_name not in DRAFT_STORE:
        raise HTTPException(status_code=404, detail="Draft not found")
    return DRAFT_STORE[user_name]


@router.post("/{user_name}")
def add_role_to_draft(user_name: str, payload: AddRoleRequest):
    service = ProfileDraftRoleService(RoleRepository())
    draft = get_draft(user_name)

    try:
        service.add_role(draft, payload.role_id)
        return {"message": "Role added", "roles": draft.roles}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{user_name}")
def remove_role_from_draft(user_name: str, payload: RemoveRoleRequest):
    service = ProfileDraftRoleService(RoleRepository())
    draft = get_draft(user_name)

    try:
        service.remove_role(draft, payload.role_id)
        return {"message": "Role removed", "roles": draft.roles}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
