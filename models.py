from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


metadata = MetaData()
Base = declarative_base()


class Weapon(Base):
    __tablename__ = 'weapon'
    metadata = metadata

    id = Column(Integer, primary_key=True)
    name = Column(String)
    damage = Column(String)
    rarity = Column(String)
    distance = Column(String)
    properties = Column(String)
    weapon_action = Column(String)
