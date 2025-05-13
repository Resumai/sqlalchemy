from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Position(Base):
    __tablename__ = "positions"

    position_id = Column(Integer, primary_key=True, autoincrement=True)
    position_name = Column(String(100), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.company_id"))


    company_link = relationship("Company", back_populates="position_link")
    worker_position_link = relationship("WorkerPosition", back_populates="position_link")



