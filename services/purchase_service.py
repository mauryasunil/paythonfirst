from repositories.purchase_repository import PurchaseRepository
from repositories.item_master_repo import ItemRepository
from repositories.supplier_repository import SupplierRepository
from database import SessionLocal

class PurchaseService:

    def __init__(self):
        self.repo = PurchaseRepository()
        self.item_repo = ItemRepository()
        self.customer_repo = SupplierRepository()

    def get_customers(self):
        with SessionLocal() as db:
            return self.customer_repo.get_all(db)

    def get_items(self,text):
        
        if not text:
            return []
        return self.item_repo.search_by_name(text)

    def get_item_details(self, item_id):
        with SessionLocal() as db:
            item = self.item_repo.get_by_id(db, item_id)
            return {
                "gst": item.gst_percent,
                "uom": item.uom,
                "hsn": item.hsn
            }
    def search_suppliers(self, text):
        if not text:
            return []
        return self.customer_repo.search_suppliers(text)

    def save_purchase(self, header, items):
        self.repo.save_purchase(header, items)
