import enum
from sqlalchemy import Boolean, Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin

class UserRole(str, enum.Enum):
    CLIENT = "client"
    MASTER = "master"
    ADMIN = "admin"

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"), default=UserRole.CLIENT, nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    specialization: Mapped[str | None] = mapped_column(String(150), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)

    master_services: Mapped[list["MasterService"]] = relationship(
        back_populates="master", cascade="all, delete-orphan"
    )
    working_hours: Mapped[list["WorkingHours"]] = relationship(
        back_populates="master", cascade="all, delete-orphan"
    )
    time_offs: Mapped[list["TimeOff"]] = relationship(
        back_populates="master", cascade="all, delete-orphan"
    )