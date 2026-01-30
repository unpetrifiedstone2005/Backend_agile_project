from fastapi import APIRouter, HTTPException
from src.api.schemas.profile_skill_req import AddSkillRequest, RemoveSkillRequest
from src.services.profileSkillService import ProfileDraftSkillService
from src.database.skill_repository import SkillRepository
from src.database.models import UserProfile

router = APIRouter(
    prefix="/profiles/draft/skills",
    tags=["Profile Draft Skills"]
)

# TEMP draft store (same pattern as role routes)
DRAFT_STORE: dict[str, UserProfile] = {}

def get_draft(user_name: str) -> UserProfile:
    if user_name not in DRAFT_STORE:
        raise HTTPException(status_code=404, detail="Draft not found")
    return DRAFT_STORE[user_name]


@router.post("/{user_name}")
def add_skill_to_draft(user_name: str, payload: AddSkillRequest):
    service = ProfileDraftSkillService(SkillRepository())
    draft = get_draft(user_name)

    try:
        service.add_skill(draft, payload.skill_id)
        return {"message": "Skill added", "skills": draft.skills}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{user_name}")
def remove_skill_from_draft(user_name: str, payload: RemoveSkillRequest):
    service = ProfileDraftSkillService(SkillRepository())
    draft = get_draft(user_name)

    try:
        service.remove_skill(draft, payload.skill_id)
        return {"message": "Skill removed", "skills": draft.skills}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
