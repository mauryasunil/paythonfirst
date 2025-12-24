from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from controllers.supplier_controller import SupplierController


class SupplierScreen(MDScreen):

    def on_pre_enter(self):
        self.controller = SupplierController()
        self.refresh_suppliers()

    def save_supplier(self):
        self.controller.add_supplier(
            name=self.ids.name.text,
            gst_no=self.ids.gst_no.text,
            phone=self.ids.phone.text,
            address=self.ids.address.text,
            supplier_type=self.ids.supplier_type.text
        )
        self.clear_fields()
        self.refresh_suppliers()

    def refresh_suppliers(self):
        self.ids.supplier_list.clear_widgets()
        suppliers = self.controller.get_all_suppliers()

        for s in suppliers:
            self.ids.supplier_list.add_widget(
                OneLineListItem(
                    text=f"{s.name} | {s.gst_no} | {s.supplier_type}| {s.phone}|{s.address}"
                )
            )

    def clear_fields(self):
        self.ids.name.text = ""
        self.ids.gst_no.text = ""
        self.ids.phone.text = ""
        self.ids.address.text = ""
        self.ids.supplier_type.text = ""
