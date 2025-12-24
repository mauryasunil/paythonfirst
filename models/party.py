
from sqlalchemy import Column,Integer,String
from database import Base
class Party(Base):
    __tablename__="parties"
    id=Column(Integer,primary_key=True)
    name=Column(String)
