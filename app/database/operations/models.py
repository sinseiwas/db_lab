from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    MetaData
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationships
)

from app.database.workers.models import User
from app.database.database import Base



class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(primary_key=True)
    p_p_number: Mapped[int] = mapped_column(Integer)
    type: Mapped[int] = mapped_column(Integer)
    worker_rank: Mapped[int] = mapped_column(ForeignKey("user.id"))
    description: Mapped[str] = mapped_column(String)
    time: Mapped[int] = mapped_column(Integer)

    detail = relationships("Detail", back_populates="operations")