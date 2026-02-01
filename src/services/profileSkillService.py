from src.database.models import ProfileDraft
from src.database.skill_repository import SkillRepository
class ProfileDraftSkillService:
    """
    Handles add/remove skill operations during profile creation.
    (no DB writes) unless create button is pressed.
    """

    def __init__(self, skill_repo: SkillRepository):
        self.skill_repo = skill_repo

    def add_skill(self, draft:ProfileDraft, skill_id: int) -> None:
        # validate skill exists in fixed DB data
        if not self.skill_repo.exists_by_id(skill_id):
            raise ValueError("Invalid skill ID")

        # prevent duplicates
        if skill_id in draft.skills:
            raise ValueError("Skill already added")

        draft.skills.append(skill_id)

    def remove_skill(self, draft:ProfileDraft, skill_id: int) -> None:
        if skill_id not in draft.skills:
            raise ValueError("Skill not present in draft")

        draft.skills.remove(skill_id)