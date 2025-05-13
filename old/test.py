from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
 
engine = create_engine("mysql://root:slapta@localhost:3306/new_schema")
 
class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    last_name = Column(String(100))


Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)


with Session() as session:
    user = Users(name = "John", last_name = "Johnest")
    session.add(user)
    session.commit()