import os
import sys

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu

# ================= RESOURCE PATH (VERY IMPORTANT) =================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ================= IMPORT SCREENS =================
from ui.screens.dashboard import DashboardScreen
from ui.screens.item_master import ItemScreen
from ui.screens.purchase import PurchaseScreen
from ui.screens.reports import ReportScreen
from ui.screens.sales import SalesScreen
from ui.screens.Ledger import LedgerScreen
from ui.screens.supplier import SupplierScreen
from ui.screens.customer import CustomerScreen

# ================= IMPORT CORE =================
from database import Base, engine
from controllers.item_controller import ItemController
from controllers.purchase_controller import PurchaseController
from controllers.report_controller import ReportController
from controllers.supplier_controller import SupplierController
from controllers.item_master_controller import ItemController
from controllers.customer_controller import CustomerController

class ERPApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"

        # ---------- Controllers ----------
        self.item_controller = ItemController()
        self.purchase_controller = PurchaseController()
        self.report_controller = ReportController()
        self.supplier_controller = SupplierController()

        # ---------- Database ----------
        Base.metadata.create_all(engine)

        # ---------- Load KV files (ORDER MATTERS) ----------
        Builder.load_file(resource_path("ui/main.kv"))
        Builder.load_file(resource_path("ui/screens/dashboard.kv"))
        Builder.load_file(resource_path("ui/screens/sales.kv"))
        Builder.load_file(resource_path("ui/screens/purchase.kv"))
        Builder.load_file(resource_path("ui/screens/item_master.kv"))
        Builder.load_file(resource_path("ui/screens/supplier.kv"))
        Builder.load_file(resource_path("ui/screens/reports.kv"))
        Builder.load_file(resource_path("ui/screens/ledger.kv"))
        Builder.load_file(resource_path("ui/screens/customer.kv"))

        # ---------- Return Root ----------
        return Builder.load_file(resource_path("ui/main.kv"))

    # ==================================================
    # NAVIGATION
    # ==================================================
    def go_dashboard(self):
        self.root.current = "dashboard"

    def go_items(self):
        self.root.current = "items"

    def go_purchase(self):
        self.root.current = "purchase"

    def go_sales(self):
        self.root.current = "sales"

    def go_ledger(self):
        self.root.current = "ledger"

    def go_reports(self):
        self.root.current = "reports"

    def go_supplier(self):
        self.root.current = "supplier"
    def go_customer(self):
        self.root.current = "customer"

    # ==================================================
    # DASHBOARD MENUS
    # ==================================================
    def open_masters_menu(self, button):
        self.masters_menu = MDDropdownMenu(
            caller=button,
            items=[
                {"text": "Item Master", "on_release": lambda: self.menu_action("items")},
                {"text": "Supplier Master", "on_release": lambda: self.menu_action("supplier")},
                {"text": "Customer Master", "on_release": lambda: self.menu_action("customer")},
            ],
            width_mult=4,
        )
        self.masters_menu.open()

    def open_transactions_menu(self, button):
        self.trans_menu = MDDropdownMenu(
            caller=button,
            items=[
                {"text": "Purchase Entry", "on_release": lambda: self.menu_action("purchase")},
                {"text": "Sales Entry", "on_release": lambda: self.menu_action("sales")},
                {"text": "Ledger", "on_release": lambda: self.menu_action("ledger")},
            ],
            width_mult=4,
        )
        self.trans_menu.open()

    def open_reports_menu(self, button):
        self.report_menu = MDDropdownMenu(
            caller=button,
            items=[
                {"text": "Stock Report", "on_release": lambda: self.menu_action("reports")},
                {"text": "Outstanding Report", "on_release": lambda: self.menu_action("reports")},
            ],
            width_mult=4,
        )
        self.report_menu.open()

    def menu_action(self, screen_name):
        for menu in ["masters_menu", "trans_menu", "report_menu"]:
            if hasattr(self, menu):
                getattr(self, menu).dismiss()
        self.root.current = screen_name

    # ==================================================
    # REPORTS
    # ==================================================
    def show_stock_report(self):
        data = self.report_controller.get_stock()
        self.root.get_screen("reports").ids.report_output.text = "\n".join(
            f"{i.name} | Stock: {i.stock}" for i in data
        )

    def show_outstanding_report(self):
        data = self.report_controller.get_outstanding()
        self.root.get_screen("reports").ids.report_output.text = "\n".join(
            f"Party {l.party_id} | Dr:{l.debit} Cr:{l.credit}" for l in data
        )


if __name__ == "__main__":
    ERPApp().run()
