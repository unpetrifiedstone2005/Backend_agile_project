#dependency injection to avoid tight coupling with data
from src.database.models import UserProfile
class FakeSkillRepository:
    def __init__(self,data):
        self.data = data
    def get_all(self):
        return self.data
    def exists_by_id(self, skill_id: int) -> bool:
        if skill_id in self.data:
            return True
        return False
    
    

class FakeRoleRepository:
    def __init__(self,data):
        self.data = data
    def get_all(self):
        return self.data
    def exists_by_id(self, role_id: int) -> bool:
        if role_id in self.data:
            return True
        return False
    
class FakeProfileRepository:
    def __init__(self, profile=None):
        self.profile = profile or {}
        self.saved_profile = None

    def create(self, profile: UserProfile):
        if profile.user_name in self.profile:
            raise ValueError("User already exists")
        self.profile[profile.user_name] = profile

    def get(self, user_name: str):
        return self.profile.get(user_name)

    def save(self, profile: UserProfile):
        self.profile[profile.user_name] = profile
        self.saved_profile = profile
        

    def exists(self, profile:UserProfile):
        return profile in self.profile
    
