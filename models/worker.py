from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from datetime import datetime as dt
from .base import Base


class Worker(Base):
    __tablename__ = "workers"
    worker_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    birth_date : dt = Column(DateTime)
    salary = Column(Integer)
    works_since : dt = Column(DateTime, default=func.now())


    worker_position_link = relationship("WorkerPosition", back_populates="worker_link")