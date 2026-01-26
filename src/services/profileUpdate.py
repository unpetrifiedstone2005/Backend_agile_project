from typing import Optional, List
from src.database.profile_repository import ProfileRepository
from src.database.skill_repository import SkillRepository
from src.database.role_repository import RoleRepository
from src.database.models import UserProfile


class ProfileUpdateService:
    def __init__(
        self,
        profile_repo: ProfileRepository,
        skill_repo: SkillRepository,
        role_repo: RoleRepository,
    ):
        self.profile_repo = profile_repo
        self.skill_repo = skill_repo
        self.role_repo = role_repo

    def update_profile(
        self,
        user_name: str,
        name: Optional[str],
        skills: Optional[List[int]],
        roles: Optional[List[int]],
    ) -> UserProfile:
        profile = self._get_existing_profile(user_name)
        self._validate_input(name, skills, roles)
        self._apply_updates(profile, name, skills, roles)
        self._save_profile(profile)
        return profile

    def _get_existing_profile(self, user_name: str) -> UserProfile:
        profile = self.profile_repo.get(user_name)
        if not profile:
            raise ValueError("Profile not found")
        return profile

    def _validate_input(
        self,
        name: Optional[str],
        skills: Optional[List[int]],
        roles: Optional[List[int]],
    ):
        if name is not None and not name.strip():
            raise ValueError("Name cannot be empty")

        if skills is not None:
            for skill_id in skills:
                if not self.skill_repo.exists_by_id(skill_id):
                    raise ValueError(f"Invalid skill ID: {skill_id}")

        if roles is not None:
            for role_id in roles:
                if not self.role_repo.exists_by_id(role_id):
                    raise ValueError(f"Invalid role ID: {role_id}")

    def _apply_updates(
        self,
        profile: UserProfile,
        name: Optional[str],
        skills: Optional[List[int]],
        roles: Optional[List[int]],
    ):
        # Username is intentionally NOT editable

        if name is not None:
            profile.name = name

        if skills is not None:
            profile.skills = list(set(skills))

        if roles is not None:
            profile.roles = list(set(roles))

    def _save_profile(self, profile: UserProfile):
        self.profile_repo.save(profile)
