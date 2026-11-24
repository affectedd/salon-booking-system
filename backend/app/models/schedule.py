from datetime import datetime, time
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Time, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class WorkingHours(Base):
    __tablename__ = "working_hours"
    __table_args__ = (
        UniqueConstraint("master_id", "day_of_week", name="uq_master_day_of_week"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    master_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    day_of_week: Mapped[int] = mapped_column(Integer, nullable=False)
    start_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)
    is_day_off: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    master: Mapped["User"] = relationship(back_populates="working_hours")


class TimeOff(Base):
    __tablename__ = "time_offs"

    id: Mapped[int] = mapped_column(primary_key=True)
    master_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    start_datetime: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_datetime: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    reason: Mapped[str | None] = mapped_column(String(255), nullable=True)

    master: Mapped["User"] = relationship(back_populates="time_offs")