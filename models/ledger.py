
from sqlalchemy import Column,Integer,Float,String
from database import Base
class Ledger(Base):
    __tablename__="ledger"
    id=Column(Integer,primary_key=True)
    party_id=Column(Integer)
    debit=Column(Float,default=0)
    credit=Column(Float,default=0)
    narration=Column(String)
