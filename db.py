from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.worker import Worker
from models.company import Company
from models.position import Position

engine = create_engine("mysql://root:slapta@localhost:3306/task_schema")

def create_database():
    Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)






