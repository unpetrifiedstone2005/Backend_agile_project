from fastapi import APIRouter, HTTPException
from src.api.schemas.profiles_req import ProfileCreateRequest
from src.services.profileCreate import ProfileCreationService
from src.database.profile_repository import ProfileRepository
from src.database.skill_repository import SkillRepository
from src.database.role_repository import RoleRepository

router = APIRouter(
    prefix="/profiles",
    tags=["Profiles"]
)

@router.post("/")
def create_profile(payload: ProfileCreateRequest):
    service = ProfileCreationService(
        profile_repo=ProfileRepository(),
        skill_repo=SkillRepository(),
        role_repo=RoleRepository(),
    )

    try:
        return service.create_profile(
            user_name=payload.user_name,
            name=payload.name,
            skills=payload.skills,
            roles=payload.roles,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
