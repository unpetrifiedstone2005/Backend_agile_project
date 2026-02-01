from abc import ABC, abstractmethod
from typing import Dict
class RoleRepository(ABC):

    @abstractmethod
    def get_all(self) -> Dict[int, str]:
        """
        Returns role_id -> role_name mapping
        """
        pass

    @abstractmethod
    def exists_by_id(self, role_id: int) -> bool:
        pass

