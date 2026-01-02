from services.purchase_service import PurchaseService

class PurchaseController:

    def __init__(self):
        self.service = PurchaseService()

    def fetch_customers(self):
        return self.service.get_customers()

    def fetch_items(self,text):
        return self.service.get_items(text)

    def fetch_item_details(self, item_id):
        return self.service.get_item_details(item_id)

    def save_purchase(self, header, items):
        self.service.save_purchase(header, items)
    def search_suppliers(self, text):
        return self.service.search_suppliers(text)
