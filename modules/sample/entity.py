from sqlalchemy import Column, Integer, String

from core.database import Base


class Sample(Base):
    __tablename__ = 'Sample'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
