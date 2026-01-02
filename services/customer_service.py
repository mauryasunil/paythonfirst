from repositories.customer_repository import CustomerRepository

class CustomerService:

    def __init__(self):
        self.repo = CustomerRepository()

    def create_customer(self, data):
        return self.repo.add(
            name=data["name"],
            mobile=data["mobile"],
            address=data["address"]
        )

    def get_customers(self):
        return self.repo.get_all()
