from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class SalesItem(Base):
    __tablename__ = "sales_items"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey("sales_invoice.id"))
    item_name = Column(String)
    hsn = Column(String)
    batch = Column(String)
    mfg = Column(String)
    exp = Column(String)
    qty = Column(Float)
    mrp = Column(Float)
    rate = Column(Float)
    discount = Column(Float)
    gst = Column(Float)
    amount = Column(Float)
