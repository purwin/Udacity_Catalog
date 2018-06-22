from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Gladiator(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    img = Column(String)
    gender = Column(String(12))
    hairdo = Column(String(20))
    main_event = Column(String(40))
    secondary_event = Column(String(40))
    accessory = Column(String(20))


engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)