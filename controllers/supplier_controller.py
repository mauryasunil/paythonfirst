from services.supplier_service import SupplierService

class SupplierController:

    def __init__(self):
        self.service = SupplierService()

    def add_supplier(self, name, gst_no, address, supplier_type,phone):
        return self.service.add_supplier(
            name, gst_no, address, supplier_type,phone
        )

    def get_all_suppliers(self):
        return self.service.get_all_suppliers()
