from sqlalchemy import(
    ForeignKey,
    Integer,
    String,
    Date,
    MetaData
)
from datetime import date
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database.database import Base
# from app.database.workers.models import Worker
from database.operations.models import Operation




class Detail(Base):
    __tablename__ = "details"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    size: Mapped[str] = mapped_column(String)
    operation_amount: Mapped[int] = mapped_column(Integer)
    start_date: Mapped[date]
    end_date: Mapped[date]
    # operations = relationship("Operation", back_populates="detail", cascade="all, delete")

