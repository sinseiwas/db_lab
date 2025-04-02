from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from sqlalchemy import (
    # ForeignKey,
    Integer,
    String,
    MetaData
)
from app.database.database import Base
from app.database.details import Detail


class Worker(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    rank: Mapped[int] = mapped_column(Integer)
    