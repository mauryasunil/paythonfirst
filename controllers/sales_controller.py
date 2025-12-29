from services.sales_service import SalesService

class SalesController:

    def __init__(self):
        self.service = SalesService()

    # def save_sales(self, header, items):
    #     self.service.create_invoice(header, items)
    def save_sales(self, header, items):
        return self.service.create_invoice(header, items)