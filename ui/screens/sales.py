from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout
from controllers.sales_controller import SalesController
from models.sales_invoice import SalesInvoice


class SalesScreen(MDScreen):

    def on_pre_enter(self):
        self.controller = SalesController()
        self.item_rows = []
        self.ids.item_table.clear_widgets()
        self.update_total(0)

    # ================= ADD ITEM ROW =================
    def add_item_row(self):
        row = MDGridLayout(
            cols=9,
            spacing=5,
            size_hint_y=None,
            height=40
        )

        fields = []

        hints = [
            "Item",
            "HSN",
            "Batch",
            "Exp",
            "Qty",
            "Rate",
            "Disc %",
            "GST %",
            "Amount"
        ]

        for i, hint in enumerate(hints):
            tf = MDTextField(
                hint_text=hint,
                size_hint_x=None,
                width=120 if i == 0 else 80,
                input_filter="float" if hint in ["Qty", "Rate", "Disc %", "GST %"] else None
            )

            # Recalculate amount when numeric fields change
            if hint in ["Qty", "Rate", "Disc %", "GST %"]:
                tf.bind(text=self.calculate_row_amount)

            fields.append(tf)
            row.add_widget(tf)

        self.item_rows.append(fields)
        self.ids.item_table.add_widget(row)

    # ================= CALCULATE ROW AMOUNT =================
    def calculate_row_amount(self, instance, value):
        total = 0

        for row in self.item_rows:
            try:
                qty = float(row[4].text or 0)
                rate = float(row[5].text or 0)
                disc = float(row[6].text or 0)
                gst = float(row[7].text or 0)

                base = qty * rate
                discount_amt = base * disc / 100
                taxable = base - discount_amt
                gst_amt = taxable * gst / 100
                amount = taxable + gst_amt

                row[8].text = f"{amount:.2f}"
                total += amount

            except ValueError:
                pass

        self.update_total(total)

    # ================= UPDATE TOTAL =================
    def update_total(self, total):
        self.ids.total_lbl.text = f"Total: ₹ {total:.2f}"


    
    

    # ================= SAVE INVOICE =================
    def save_invoice(self):
        header = {
            # "invoice_no":  invoice_no,
            "customer_name": self.ids.customer_name.text,
            "customer_mobile": self.ids.mobile.text,
            "customer_address": self.ids.address.text
        }

        items = []

        for row in self.item_rows:
            try:
                item = {
                    "item_name": row[0].text,
                    "hsn": row[1].text,
                    "batch": row[2].text,
                    "exp": row[3].text,
                    "qty": float(row[4].text or 0),
                    "rate": float(row[5].text or 0),
                    "discount": float(row[6].text or 0),
                    "gst": float(row[7].text or 0),
                    "amount": float(row[8].text or 0),
                }
                items.append(item)
            except ValueError:
                pass

        self.controller.save_sales(header, items)
