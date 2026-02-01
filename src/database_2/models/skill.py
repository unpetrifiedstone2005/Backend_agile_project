from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from src.database_2.base import Base

class Skill(Base):
    __tablename__ = "skills"

    skill_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    skill_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    students = relationship(
        "StudentSkill",
        back_populates="skill",
        cascade="all, delete"
    )
