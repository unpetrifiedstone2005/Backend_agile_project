from src.database.models import UserProfile
class ProfileDraftRoleService:
    """
    Handles add/remove role operations during profile creation.
    Works ONLY on ProfileDraft (no DB writes).
    """

    def __init__(self, role_repo):
        self.role_repo = role_repo

    def add_role(self, draft:UserProfile, role_id: int) -> None:
        # validate role exists in fixed DB data
        if not self.role_repo.exists_by_id(role_id):
            raise ValueError("Invalid role ID")

        # prevent duplicates
        if role_id in draft.roles:
            raise ValueError("Role already added")

        draft.roles.append(role_id)

    def remove_role(self, draft:UserProfile, role_id: int) -> None:
        if role_id not in draft.roles:
            raise ValueError("Role not present in draft")

        draft.roles.remove(role_id)
