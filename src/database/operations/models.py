from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    MetaData
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

# from database.workers.models import Worker
from database.database import Base



class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(primary_key=True)
    p_p_number: Mapped[int] = mapped_column(Integer)
    type: Mapped[int] = mapped_column(Integer)
    worker_rank: Mapped[int] = mapped_column(ForeignKey("workers.id"))
    description: Mapped[str] = mapped_column(String)
    time: Mapped[int] = mapped_column(Integer)

    # detail = relationship("Detail", back_populates="operations")