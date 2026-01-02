from services.customer_service import CustomerService

class CustomerController:

    def __init__(self):
        self.service = CustomerService()

    def save_customer(self, data):
        return self.service.create_customer(data)

    def fetch_customers(self):
        return self.service.get_customers()
