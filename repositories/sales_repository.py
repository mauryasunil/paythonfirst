# sales_repository.py
from database import SessionLocal
from models.sales_invoice import SalesInvoice
from models.sales_items import SalesItem

class SalesRepository:

    def save_invoice(self, invoice_data, items_data):
        db = SessionLocal()

        invoice = SalesInvoice(**invoice_data)
        db.add(invoice)
        db.commit()
        db.refresh(invoice)

        for item in items_data:
            db_item = SalesItem(
                
                **item
            )
            db.add(db_item)

        db.commit()

        # 🔴 VERY IMPORTANT: convert to plain dict
        invoice_dict = {
            "id": invoice.id,
            "invoice_no": invoice.invoice_no,
            "customer_name": invoice.customer_name,
            "customer_mobile": invoice.customer_mobile,
            "address": invoice.customer_address,
           
        }

        db.close()
        return invoice_dict
