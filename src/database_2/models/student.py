from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from src.database_2.base import Base

class Student(Base):
    __tablename__ = "students"

    username: Mapped[str] = mapped_column(
        String(50),
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # relationships
    skills = relationship(
        "StudentSkill",
        back_populates="student",
        cascade="all, delete"
    )

    roles = relationship(
        "StudentRole",
        back_populates="student",
        cascade="all, delete"
    )
