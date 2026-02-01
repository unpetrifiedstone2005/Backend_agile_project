from abc import ABC, abstractmethod

class ProfileRepository(ABC):

    @abstractmethod
    def save(self, profile):
        pass

    @abstractmethod
    def get(self, user_name: str):
        pass

    @abstractmethod
    def exists(self, user_name: str) -> bool:
        pass

    @abstractmethod
    def has_skill(self, user_name: str, skill_id: int) -> bool:
        pass

    