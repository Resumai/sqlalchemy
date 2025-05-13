from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class Position(Base):
    __tablename__ = "positions"

    position_id = Column(Integer, primary_key=True, autoincrement=True)
    position_name = Column(String(100), nullable=False)
    worker_id = Column(Integer, ForeignKey("workers.worker_id"))
    company_id = Column(Integer, ForeignKey("companies.company_id"))


    worker_link = relationship("Worker", back_populates="position_link")
    company_link = relationship("Company", back_populates="position_link")




