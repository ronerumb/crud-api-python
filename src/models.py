from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.sql import func
from db import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'
    id = Column(Integer , primary_key= True)
    name = Column(String)
    type = Column(String)
    creted_at = Column(DateTime , default = func.now())