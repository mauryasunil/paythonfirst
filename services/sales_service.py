from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4
from models.sales_invoice import SalesInvoice
from models.sales_items import SalesItem
from repositories.sales_repository import SalesRepository

class SalesService:

    def __init__(self):
        self.repo = SalesRepository()

    def create_invoice(self, header, items):
        total = sum(i["amount"] for i in items)
        cgst = sgst = total * 0.09
        grand_total = total + cgst + sgst

        invoice = SalesInvoice(
            invoice_no=header["invoice_no"],
            customer_name=header["customer_name"],
            customer_mobile=header["customer_mobile"],
            customer_address=header["customer_address"],
            total_amount=total,
            cgst=cgst,
            sgst=sgst,
            igst=0,
            grand_total=grand_total
        )

        # item_objs = [SalesItem(**i) for i in items]
        invoice_dict = self.repo.save_invoice(header, items)

        self.export_excel(invoice_dict, items)
      

    def export_excel(self, invoice, items):
        wb = Workbook()
        ws = wb.active
        ws.title = "Sales Invoice"

        ws.append(["Invoice No", invoice.invoice_no])
        ws.append(["Customer", invoice.customer_name])
        ws.append(["Mobile", invoice.customer_mobile])
        ws.append(["Address", invoice.customer_address])
        ws.append([])

        ws.append(["Item","HSN","Batch","MFG","EXP","Qty","Rate","Disc","Amount"])

        for i in items:
            ws.append([
                i["item_name"], i["hsn"], i["batch"],
                i["mfg"], i["exp"], i["qty"],
                i["rate"], i["discount"], i["amount"]
            ])

        ws.append([])
        ws.append(["CGST 9%", invoice.cgst])
        ws.append(["SGST 9%", invoice.sgst])
        ws.append(["GRAND TOTAL", invoice.grand_total])

        wb.save(f"Invoice_{invoice.invoice_no}.xlsx")
    
