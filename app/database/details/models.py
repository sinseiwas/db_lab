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

from database import Base
# from app.database.workers.models import Worker
# from app.database.operations.models import Operation


metadata_obj = MetaData()


class Detail(Base):
    __tablename__ = "details"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    size: Mapped[str] = mapped_column(String)
    operation_amount: Mapped[int] = mapped_column(Integer)
    date: Mapped[date]

    operations = relationship("Operation", back_populates="detail", cascade="all, delete")

