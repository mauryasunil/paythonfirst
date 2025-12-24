from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class SalesInvoice(Base):
    __tablename__ = "sales_invoice"

    id = Column(Integer, primary_key=True)
    invoice_no = Column(String, unique=True)
    customer_name = Column(String)
    customer_mobile = Column(String)
    customer_address = Column(String)
    total_amount = Column(Float)
    cgst = Column(Float)
    sgst = Column(Float)
    igst = Column(Float)
    grand_total = Column(Float)
