from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class WorkerPosition(Base):
    __tablename__ = "worker_position"    
    worker_id = Column(Integer, ForeignKey("workers.worker_id"), primary_key=True)
    position_id = Column(Integer, ForeignKey("positions.position_id"), primary_key=True)
    

    worker_link = relationship("Worker", back_populates="worker_position_link")
    position_link = relationship("Position", back_populates="worker_position_link")