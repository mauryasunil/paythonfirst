from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from controllers.sales_controller import SalesController


class SalesScreen(MDScreen):

    def on_pre_enter(self):
        self.controller = SalesController()
        self.item_rows = []
        self.ids.item_table.clear_widgets()
        self.update_total(0)

    # ================= ADD ITEM ROW =================
    def add_item_row(self):
        row = MDGridLayout(
            cols=10,   # ✅ UPDATED
            spacing=5,
            size_hint_y=None,
            height=40
        )

        fields = []
        hints = [
            "Item", "HSN", "Batch", "Exp",
            "Qty", "MRP", "Rate", "Disc %", "GST %", "Amount"
        ]

        for i, hint in enumerate(hints):
            tf = MDTextField(
                hint_text=hint,
                size_hint_x=None,
                width=120 if i == 0 else 80,
                input_filter="float" if hint in ["Qty", "MRP", "Rate", "Disc %", "GST %"] else None
            )

            if hint in ["Qty", "Rate", "Disc %", "GST %"]:
                tf.bind(text=self.calculate_row_amount)

            if hint == "MRP":
                tf.bind(text=self.calculate_rate_from_mrp)

            fields.append(tf)
            row.add_widget(tf)

        self.item_rows.append(fields)
        self.ids.item_table.add_widget(row)

    # ================= MRP → RATE =================
    def calculate_rate_from_mrp(self, instance, value):
        for row in self.item_rows:
            if instance not in row:
                continue

            try:
                MRP = float(row[5].text or 0)
                gst = float(row[8].text or 0)

                if MRP > 0 and gst >= 0:
                    rate = (MRP * 100) / (100 + gst)
                    row[6].text = f"{rate:.2f}"

            except ValueError:
                pass

        self.calculate_row_amount(None, None)

    # ================= CALCULATE ROW AMOUNT =================
    def calculate_row_amount(self, instance, value):
        total = 0

        for row in self.item_rows:
            try:
                qty = float(row[4].text or 0)
                rate = float(row[6].text or 0)
                disc = float(row[7].text or 0)
                gst = float(row[8].text or 0)

                base = qty * rate
                discount_amt = base * disc / 100
                taxable = base - discount_amt
                gst_amt = taxable * gst / 100
                amount = taxable + gst_amt

                row[9].text = f"{amount:.2f}"
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
            "customer_name": self.ids.customer_name.text,
            "customer_mobile": self.ids.mobile.text,
            "customer_address": self.ids.address.text
        }

        items = []
        for row in self.item_rows:
            if not row[0].text:
                continue

            items.append({
                "item_name": row[0].text,
                "hsn": row[1].text,
                "batch": row[2].text,
                "exp": row[3].text,
                "qty": float(row[4].text or 0),
                "mrp": float(row[5].text or 0),   # ✅ NEW
                "rate": float(row[6].text or 0),
                "discount": float(row[7].text or 0),
                "gst": float(row[8].text or 0),
                "amount": float(row[9].text or 0),
            })

        if not items:
            return

        invoice = self.controller.save_sales(header, items)

        self.show_success_popup(invoice["invoice_no"])
        self.clear_form()

    # ================= SUCCESS POPUP =================
    def show_success_popup(self, invoice_no):
        self.dialog = MDDialog(
            title="Invoice Saved",
            text=f"Invoice {invoice_no} saved successfully!",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.close_dialog()
                )
            ],
        )
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss()

    # ================= CLEAR FORM =================
    def clear_form(self):
        self.ids.customer_name.text = ""
        self.ids.mobile.text = ""
        self.ids.address.text = ""
        self.ids.item_table.clear_widgets()
        self.item_rows = []
        self.update_total(0)
