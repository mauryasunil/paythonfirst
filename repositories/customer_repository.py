from database import SessionLocal
from models.customer import Customer

class CustomerRepository:

    @staticmethod
    def add(name, mobile, address):
        db = SessionLocal()
        customer = Customer(
            name=name,
            mobile=mobile,
            address=address
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)
        db.close()
        return customer

    @staticmethod
    def get_all():
        db = SessionLocal()
        data = db.query(Customer).all()
        db.close()
        return data
    def search_suppliers(self, text):
        db = SessionLocal()
        result = (
            db.query(Customer)
            .filter(Customer.name.ilike(f"%{text}%"))
            .all()
        )
        db.close()
        return result
