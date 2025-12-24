from repositories.supplier_repository import SupplierRepository


from repositories.supplier_repository import SupplierRepository

class SupplierService:

    def __init__(self):
        self.repo = SupplierRepository()

    def add_supplier(self, name, gst_no, address, supplier_type,phone):
        return self.repo.add_supplier(
            name=name,
            gst_no=gst_no,
            address=address,
            supplier_type=supplier_type,
            phone=phone
        )

    def get_all_suppliers(self):
        return self.repo.fetch_all()
