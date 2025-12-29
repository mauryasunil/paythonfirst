from database import SessionLocal
from models.sales_invoice import SalesInvoice
from models.sales_items import SalesItem


class SalesRepository:

    def generate_next_invoice(self, db):
        last = (
            db.query(SalesInvoice)
            .order_by(SalesInvoice.id.desc())
            .first()
        )

        if last and last.invoice_no:
            last_no = int(last.invoice_no.replace("INV-", ""))
            next_no = last_no + 1
        else:
            next_no = 1

        return f"INV-{next_no:06d}"

    def save_invoice(self, header, items_data):
        db = SessionLocal()
        try:
            # 🔹 generate invoice number
            invoice_no = self.generate_next_invoice(db)
            header["invoice_no"] = invoice_no

            # 🔹 save invoice
            invoice = SalesInvoice(**header)
            db.add(invoice)
            db.commit()
            db.refresh(invoice)

            # 🔹 save items
            for item in items_data:
                item["invoice_id"] = invoice.id
                db.add(SalesItem(**item))

            db.commit()

            # 🔹 convert ORM → dict BEFORE session close
            invoice_dict = {
                "invoice_no": invoice.invoice_no,
                "customer_name": invoice.customer_name,
                "customer_mobile": invoice.customer_mobile,
                "customer_address": invoice.customer_address,
                "total_amount": invoice.total_amount,
                "cgst": invoice.cgst,
                "sgst": invoice.sgst,
                "grand_total": invoice.grand_total,
            }

            return invoice_dict

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()
