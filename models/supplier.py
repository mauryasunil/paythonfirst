from sqlalchemy import Column, Integer, String
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gst_no = Column(String)
    address = Column(String)
    supplier_type = Column(String)   # Local / Interstate / Import
    phone = Column(String)
