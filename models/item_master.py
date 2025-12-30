
from sqlalchemy import Column,Integer,String,Float
from database import Base
class Item(Base):
    __tablename__="itemsmaster"
    id=Column(Integer,primary_key=True)
    item_name=Column(String)
    Descreptio=Column(String)
    category=Column(String(30))
    sub_category=Column(String(30))
    uom = Column(String(20))
    gst_percent = Column(Float)
    hsn = Column(Float)
   
            