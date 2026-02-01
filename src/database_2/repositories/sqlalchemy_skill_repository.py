from sqlalchemy.orm import Session
from src.database.skill_repository import SkillRepository
from src.database.models import Skill

class SQLAlchemySkillRepository(SkillRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        skills = self.db.query(Skill).all()
        return {skill.skill_id: skill.skill_name for skill in skills}

    def exists_by_id(self, skill_id: int) -> bool:
        return (
            self.db
            .query(Skill)
            .filter(Skill.skill_id == skill_id)
            .first()
            is not None
        )
