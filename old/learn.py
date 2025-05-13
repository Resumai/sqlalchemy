from sqlalchemy import create_engine, select, Column, Integer, String, DateTime, or_
from sqlalchemy.orm import DeclarativeBase, sessionmaker
 
engine = create_engine("mysql://root:slapta@localhost:3306/new_schema")
 
class Base(DeclarativeBase):
    pass

class Device(Base):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column (String(50), nullable=False)
    created_at = Column(DateTime)
 
class Shop(Base):
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column (String(50), nullable=False)
    created_at = Column(DateTime)



Base.metadata.create_all(engine)


Session = sessionmaker(bind= engine)

# crud

# with Session() as session:
#     new_shop = Shop(name = "Tavo Parduotuve123")
#     session.add(new_shop)
#     session.commit()

# with Session() as session:
#     shop = session.get(Shop, 1)
#     if shop:
#         print(shop.name)


# with Session() as session:
#     query = select(Shop).filter_by(name = "Electromart")
#     shop = session.execute(query).scalar_one()

#     if shop:
#         print(shop.name)



# with Session() as session:
#     query = select(Shop).filter_by(name = "Electromart")
#     shops = session.execute(query).scalars().all()

#     for shop in shops:
#         print(shop.id, shop.name)

# with Session() as session:
#     query = select(Shop).where(Shop.id >= 2)
#     shops = session.execute(query).scalars().all()

#     for shop in shops:
#         print(shop.id, shop.name)


# with Session() as session:
#     query = select(Shop).where(Shop.name.ilike("T%"))
#     shops = session.execute(query).scalars().all()

#     for shop in shops:
#         print(shop.id, shop.name)


# with Session() as session:
#     query = select(Shop).filter_by(name = "Electromart")
#     shops = session.execute(query).scalars().all()

#     for shop in shops:
#         print(shop.id, shop.name)
#         shop.name = "Elektromarkt"
#         session.commit()


with Session() as session:
    query = select(Shop).where(or_(Shop.id == 4, Shop.id == 5))
    shops = session.execute(query).scalars().all()

    for shop in shops:
        session.delete(shop)
        session.commit()
        # print(shop.id, shop.name)