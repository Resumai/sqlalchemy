from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base



class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(100), nullable=False)
    

    position_link = relationship("Position", back_populates="company_link")


