from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database_2.base import Base

class StudentSkill(Base):
    __tablename__ = "student_skills"

    username: Mapped[str] = mapped_column(
        ForeignKey("students.username"),
        primary_key=True
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("skills.skill_id"),
        primary_key=True
    )

    student = relationship("Student", back_populates="skills")
    skill = relationship("Skill", back_populates="students")
