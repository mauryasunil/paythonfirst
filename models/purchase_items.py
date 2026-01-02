from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer)
    product_id = Column(Integer)

    batch = Column(String)
    mfg_date = Column(Date)
    exp_date = Column(Date)

    qty = Column(Float)
    rate = Column(Float)
    gst_percent = Column(Float)
    amount = Column(Float)
