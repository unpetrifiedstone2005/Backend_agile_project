from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database_2.base import Base

class StudentRole(Base):
    __tablename__ = "student_roles"

    username: Mapped[str] = mapped_column(
        ForeignKey("students.username"),
        primary_key=True
    )

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.role_id"),
        primary_key=True
    )

    student = relationship("Student", back_populates="roles")
    role = relationship("Role", back_populates="students")
