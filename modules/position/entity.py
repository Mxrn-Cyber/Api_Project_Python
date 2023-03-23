from sqlalchemy import Column, Integer, String

from core.database import Base


class Position(Base):
    __tablename__ = 'Position'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
