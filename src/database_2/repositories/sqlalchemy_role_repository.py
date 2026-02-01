from sqlalchemy.orm import Session
from src.database.role_repository import RoleRepository
from src.database.models import Role

class SQLAlchemyRoleRepository(RoleRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        roles = self.db.query(Role).all()
        return {role.role_id: role.role_name for role in roles}

    def exists_by_id(self, role_id: int) -> bool:
        return (
            self.db
            .query(Role)
            .filter(Role.role_id == role_id)
            .first()
            is not None
        )
