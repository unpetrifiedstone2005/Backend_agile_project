from sqlalchemy.orm import Session
from src.database.profile_repository import ProfileRepository
from src.database.models import Student, StudentSkill

class SQLAlchemyProfileRepository(ProfileRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, profile):
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def get(self, user_name: str):
        return (
            self.db
            .query(Student)
            .filter(Student.username == user_name)
            .first()
        )

    def exists(self, user_name: str) -> bool:
        return (
            self.db
            .query(Student)
            .filter(Student.username == user_name)
            .first()
            is not None
        )

    def has_skill(self, user_name: str, skill_id: int) -> bool:
        return (
            self.db
            .query(StudentSkill)
            .filter(
                StudentSkill.username == user_name,
                StudentSkill.skill_id == skill_id
            )
            .first()
            is not None
        )
