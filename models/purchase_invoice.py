from sqlalchemy import Column, Integer, String, Date
from database import Base

class PurchaseInvoice(Base):
    __tablename__ = "purchase_invoice"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer)
    invoice_no = Column(String)
    invoice_date = Column(Date)
