#Single Responsibility Principle
from src.database.profile_repository import ProfileRepository
from src.database.skill_repository import SkillRepository
from src.database.role_repository import RoleRepository
from src.database.models import UserProfile


class ProfileCreationService:
    def __init__(
        self,
        profile_repo: ProfileRepository,
        skill_repo: SkillRepository,
        role_repo: RoleRepository,
    ):
        self.profile_repo = profile_repo
        self.skill_repo = skill_repo
        self.role_repo = role_repo

    def create_profile(
        self,
        user_name: str,
        name: str,
        skills: list[int],
        roles: list[int],
    ) -> UserProfile:
        self._validate_input(user_name, name, skills, roles)
        self._check_uniqueness(user_name)
        profile = self._build_profile(user_name, name, skills, roles)
        self._save_profile(profile)
        return profile

    def _validate_input(self, user_name, name, skills, roles):
        if not user_name:
            raise ValueError("Username is required")

        if not name:
            raise ValueError("Name is required")

        if not skills:
            raise ValueError("At least one skill is required")

        if not roles:
            raise ValueError("At least one role is required")

        for skill_id in skills:
            if not self.skill_repo.exists_by_id(skill_id):
                raise ValueError(f"Invalid skill ID: {skill_id}")

        for role_id in roles:
            if not self.role_repo.exists_by_id(role_id):
                raise ValueError(f"Invalid role ID: {role_id}")

    def _check_uniqueness(self, user_name):
        if self.profile_repo.exists(user_name):
            raise ValueError("User already exists")
    
    def _build_profile(self, user_name, name, skills, roles):
        return UserProfile(
            user_name=user_name,
            name=name,
            skills=list(set(skills)),
            roles=list(set(roles)),
        )
    
    def _save_profile(self, profile):
        self.profile_repo.save(profile)

