from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from controllers.purchase_controller import PurchaseController


class PurchaseScreen(MDScreen):

    def on_pre_enter(self):
        self.controller = PurchaseController()
        self.items = []
        self.supplier_menu = None
        self.item_menus = {}

    # ================= SUPPLIER AUTO SEARCH =================
    def on_supplier_text(self, text):
        if not text:
            return

        suppliers = self.controller.search_suppliers(text)

        menu_items = [{
            "text": s.name,
            "on_release": lambda x=s: self.set_supplier(x)
        } for s in suppliers]

        if self.supplier_menu:
            self.supplier_menu.dismiss()

        self.supplier_menu = MDDropdownMenu(
            caller=self.ids.supplier,
            items=menu_items,
            width_mult=4
        )
        self.supplier_menu.open()

    def set_supplier(self, supplier):
        self.ids.supplier.text = supplier.name
        if self.supplier_menu:
            self.supplier_menu.dismiss()

    # ================= ITEM ROW =================
    def add_item_row(self):
        row = []

        item_tf = MDTextField(hint_text="Item", size_hint_x=None, width=140)
        item_tf.bind(text=lambda inst, val: self.on_item_text(inst, val))
        self.ids.item_table.add_widget(item_tf)
        row.append(item_tf)

        hsn = MDTextField(size_hint_x=None, width=80)
        self.ids.item_table.add_widget(hsn)
        row.append(hsn)

        batch = MDTextField(size_hint_x=None, width=90)
        self.ids.item_table.add_widget(batch)
        row.append(batch)

        mfg = MDTextField(size_hint_x=None, width=90)
        self.ids.item_table.add_widget(mfg)
        row.append(mfg)

        expiry = MDTextField(size_hint_x=None, width=90)
        self.ids.item_table.add_widget(expiry)
        row.append(expiry)

        qty = MDTextField(size_hint_x=None, width=70)
        self.ids.item_table.add_widget(qty)
        row.append(qty)

        rate = MDTextField(size_hint_x=None, width=80)
        self.ids.item_table.add_widget(rate)
        row.append(rate)

        gst = MDTextField(size_hint_x=None, width=70)
        self.ids.item_table.add_widget(gst)
        row.append(gst)

        self.items.append(row)

    # ================= ITEM AUTO SEARCH =================
    def on_item_text(self, textfield, value):
        if not value:
            return

        items = self.controller.fetch_items(value)

        menu_items = [{
            "text": i.item_name,
            "on_release": lambda x=i, tf=textfield: self.set_item(tf, x)
        } for i in items]

        if textfield in self.item_menus:
            self.item_menus[textfield].dismiss()

        menu = MDDropdownMenu(
            caller=textfield,
            items=menu_items,
            width_mult=4
        )
        self.item_menus[textfield] = menu
        menu.open()

    def set_item(self, textfield, item):
        row = next(r for r in self.items if r[0] == textfield)

        row[0].text = str(item.item_name or "")
        row[1].text = str(item.hsn or "")
        row[7].text = str(item.gst_percent or 0)

        self.item_menus[textfield].dismiss()

    # ================= SAVE PURCHASE =================
    def save_purchase(self):
        header = {
            "invoice_no": self.ids.invoice_no.text,
            "supplier_id": self.ids.supplier.text,
            "date": self.ids.date.text
        }

        items = []
        total = 0

        for r in self.items:
            qty = float(r[5].text or 0)
            rate = float(r[6].text or 0)
            gst = float(r[7].text or 0)

            base = qty * rate
            gst_amt = base * gst / 100
            total_amt = base + gst_amt
            total += total_amt

            items.append({
                "item_name": r[0].text,
                "hsn": r[1].text,
                "batch": r[2].text,
                "mfg": r[3].text,
                "expiry": r[4].text,
                "qty": qty,
                "rate": rate,
                "gst": gst,
                "amount": total_amt
            })

        self.ids.total_lbl.text = f"Total: {total:.2f}"
        self.controller.save_purchase(header, items)
        self.clear_form()

    def clear_form(self):
        self.ids.invoice_no.text = ""
        self.ids.supplier.text = ""
        self.ids.date.text = ""
        self.ids.item_table.clear_widgets()
        self.items = []
