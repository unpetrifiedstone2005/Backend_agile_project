from abc import ABC, abstractmethod
from typing import Dict
class SkillRepository(ABC):

    @abstractmethod
    def get_all(self) -> Dict[int, str]:
        """
        Returns skill_id -> skill_name mapping
        """
        pass

    @abstractmethod
    def exists_by_id(self, skill_id: int) -> bool:
        pass
