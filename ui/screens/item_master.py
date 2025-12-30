from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineListItem
from controllers.item_master_controller import ItemController

CATEGORY_MAP = {
    "Pesticide": ["Insecticide", "Herbicide", "Fungicide"],
    "Fertilizer": ["Urea", "DAP", "Potash"],
    "Seeds": ["Hybrid", "Local"]
}

UOMS = ["PCS", "KG", "LTR", "BAG"]
GST_RATES = ["0", "5", "12", "18", "28"]


class ItemScreen(MDScreen):

    def on_pre_enter(self):
        self.controller = ItemController()
        self.category_menu = None
        self.subcategory_menu = None
        self.uom_menu = None
        self.gst_menu = None
        self.load_items()

    # ---------- CATEGORY ----------
    def open_category_menu(self, caller):
        self.category_menu = MDDropdownMenu(
            caller=caller,
            items=[{
                "text": c,
                "on_release": lambda x=c: self.set_category(x)
            } for c in CATEGORY_MAP],
            width_mult=4
        )
        self.category_menu.open()

    def set_category(self, value):
        self.ids.category.text = value
        if "subcategory" in self.ids:
            self.ids.subcategory.text = ""
        self.category_menu.dismiss()

    # ---------- SUB CATEGORY ----------
    def open_subcategory_menu(self, caller):
        category = self.ids.category.text
        if category not in CATEGORY_MAP:
            return

        self.subcategory_menu = MDDropdownMenu(
            caller=caller,
            items=[{
                "text": s,
                "on_release": lambda x=s: self.set_subcategory(x)
            } for s in CATEGORY_MAP[category]],
            width_mult=4
        )
        self.subcategory_menu.open()

    def set_subcategory(self, value):
        self.ids.subcategory.text = value
        self.subcategory_menu.dismiss()

    # ---------- UOM ----------
    def open_uom_menu(self, caller):
        self.uom_menu = MDDropdownMenu(
            caller=caller,
            items=[{
                "text": u,
                "on_release": lambda x=u: self.set_uom(x)
            } for u in UOMS],
            width_mult=3
        )
        self.uom_menu.open()

    def set_uom(self, value):
        self.ids.uom.text = value
        self.uom_menu.dismiss()

    # ---------- GST ----------
    def open_gst_menu(self, caller):
        self.gst_menu = MDDropdownMenu(
            caller=caller,
            items=[{
                "text": g,
                "on_release": lambda x=g: self.set_gst(x)
            } for g in GST_RATES],
            width_mult=3
        )
        self.gst_menu.open()

    def set_gst(self, value):
        self.ids.gst.text = value
        self.gst_menu.dismiss()

    # ---------- SAVE ----------
    def save_item(self):
        data = {
            "item_name": self.ids.item_name.text,
            "category": self.ids.category.text,
            "sub_category": self.ids.subcategory.text,
            "uom": self.ids.uom.text,
            "gst_percent": float(self.ids.gst.text or 0),
            "hsn": self.ids.hsn.text,
            "Descreptio": self.ids.descreption.text
        }
        self.controller.save_item(data)
        self.clear_fields()
        self.load_items()

    def load_items(self):
        self.ids.item_list.clear_widgets()
        for i in self.controller.get_items():
            self.ids.item_list.add_widget(
                OneLineListItem(
                    text=f"{i.item_name} | {i.category}/{i.sub_category} | {i.uom} | GST {i.gst_percent} | {i.hsn} | {i.Descreptio}%"
                )
            )

    def clear_fields(self):
        self.ids.item_name.text = ""
        self.ids.category.text = ""
        self.ids.subcategory.text = ""
        self.ids.uom.text = ""
        self.ids.gst.text = ""
        self.ids.hsn.text=""
        self.ids.descreption.text=""
