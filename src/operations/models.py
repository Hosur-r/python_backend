from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, TIMESTAMP

from src.database import Base

class Operation(Base):
    __tablename__ = 'operations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[str]
    penis:Mapped[str]
    figi:Mapped[str]
    instrument_type:Mapped[str] = mapped_column(String, nullable=True)
    date:Mapped[datetime.timestamp] = mapped_column(TIMESTAMP)
    type:Mapped[str]
