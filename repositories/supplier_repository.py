from database import SessionLocal
from models.supplier import Supplier

class SupplierRepository:

    @staticmethod
    def add_supplier(name, gst_no, address, supplier_type,phone):
        db = SessionLocal()
        supplier = Supplier(
            name=name,
            gst_no=gst_no,
            address=address,
            supplier_type=supplier_type,
            phone=phone
        )
        db.add(supplier)
        db.commit()
        db.refresh(supplier)
        db.close()
        return supplier

    @staticmethod
    def fetch_all():
        db = SessionLocal()
        data = db.query(Supplier).all()
        db.close()
        return data
