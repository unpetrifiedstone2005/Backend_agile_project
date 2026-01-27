from fastapi import APIRouter, HTTPException
from src.api.schemas.profile_update_req import ProfileUpdateRequest
from src.services.profileUpdate import ProfileUpdateService
from src.database.profile_repository import ProfileRepository
from src.database.skill_repository import SkillRepository
from src.database.role_repository import RoleRepository

router = APIRouter(
    prefix="/profiles",
    tags=["Profiles"]
)

@router.put("/{user_name}")
def update_profile(user_name: str, payload: ProfileUpdateRequest):
    service = ProfileUpdateService(
        profile_repo=ProfileRepository(),
        skill_repo=SkillRepository(),
        role_repo=RoleRepository(),
    )

    try:
        return service.update_profile(
            user_name=user_name,
            name=payload.name,
            skills=payload.skills,
            roles=payload.roles,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
