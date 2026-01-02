from database import SessionLocal
from models.purchase_invoice import PurchaseInvoice
from models.purchase_items import PurchaseItem

class PurchaseRepository:

    def save_purchase(self, header, items):
        db = SessionLocal()

        invoice = PurchaseInvoice(
            supplier_id=header["supplier_id"],
            invoice_no=header["invoice_no"]
        )
        db.add(invoice)
        db.commit()
        db.refresh(invoice)

        for i in items:
            db_item = PurchaseItem(
                invoice_id=invoice.id,
                product_id=i["item_name"],
                batch=i["batch"],
                mfg_date=i["mfg"],
                exp_date=i["expiry"],
                qty=i["qty"],
                rate=i["rate"],
                gst_percent=i["gst"]
            )
            db.add(db_item)

        db.commit()
        db.close()
