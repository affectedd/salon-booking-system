from decimal import Decimal
from sqlalchemy import Boolean, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, TimestampMixin


class Service(Base, TimestampMixin):
    __tablename__ = "services"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    master_associations: Mapped[list["MasterService"]] = relationship(
        back_populates="service", cascade="all, delete-orphan"
    )


class MasterService(Base):
    __tablename__ = "master_services"
    __table_args__ = (
        UniqueConstraint("master_id", "service_id", name="uq_master_service"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    master_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id", ondelete="CASCADE"), nullable=False)

    custom_price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    custom_duration_minutes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    master: Mapped["User"] = relationship(back_populates="master_services")
    service: Mapped["Service"] = relationship(back_populates="master_associations")