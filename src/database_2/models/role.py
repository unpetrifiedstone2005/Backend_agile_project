from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from src.database_2.base import Base

class Role(Base):
    __tablename__ = "roles"

    role_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    role_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    students = relationship(
        "StudentRole",
        back_populates="role",
        cascade="all, delete"
    )
