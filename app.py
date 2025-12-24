from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu

# 🔴 IMPORTANT: Import Screen classes FIRST
from ui.screens.dashboard import DashboardScreen
from ui.screens.item_master import ItemScreen
from ui.screens.purchase import PurchaseScreen
from ui.screens.reports import ReportScreen
from ui.screens.sales import SalesScreen
from ui.screens.Ledger import LedgerScreen
from ui.screens.supplier import SupplierScreen

from database import Base, engine
from controllers.item_controller import ItemController
from controllers.purchase_controller import PurchaseController
from controllers.report_controller import ReportController
from controllers.supplier_controller import SupplierController

class ERPApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"

        # ---------- Controllers ----------
        self.item_controller = ItemController()
        self.purchase_controller = PurchaseController()
        self.report_controller = ReportController()
        self.supplier_controller = SupplierController()


        # ---------- DB ----------
        Base.metadata.create_all(engine)

        # ---------- Load KV files (ORDER MATTERS) ----------
        Builder.load_file("ui/screens/dashboard.kv")
        Builder.load_file("ui/screens/item_master.kv")
        Builder.load_file("ui/screens/purchase.kv")
        Builder.load_file("ui/screens/sales.kv")
        Builder.load_file("ui/screens/ledger.kv")
        Builder.load_file("ui/screens/reports.kv")
        Builder.load_file("ui/screens/supplier.kv")


        # ---------- Load main ----------
        return Builder.load_file("ui/main.kv")

    # ==================================================
    # BASIC NAVIGATION
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


    # ==================================================
    # DASHBOARD DROPDOWN MENUS
    # ==================================================
    def open_masters_menu(self, button):
        menu_items = [
            {
                "text": "Item Master",
                "on_release": lambda: self.menu_action("items")
            },
            {
                "text": "Supplier Master",
                "on_release": lambda: self.menu_action("supplier")
            }
        ]
        self.masters_menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=4
        )
        self.masters_menu.open()

    def open_transactions_menu(self, button):
        menu_items = [
            {
                "text": "Purchase Entry",
                "on_release": lambda: self.menu_action("purchase")
            },
            {
                "text": "Sales Entry",
                "on_release": lambda: self.menu_action("sales")
            },
            {
                "text": "Ledger",
                "on_release": lambda: self.menu_action("ledger")
            }
        ]
        self.trans_menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=4
        )
        self.trans_menu.open()

    def open_reports_menu(self, button):
        menu_items = [
            {
                "text": "Stock Report",
                "on_release": lambda: self.menu_action("reports")
            },
            {
                "text": "Outstanding Report",
                "on_release": lambda: self.menu_action("reports")
            }
        ]
        self.report_menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=4
        )
        self.report_menu.open()

    def menu_action(self, screen_name):
        for menu in ["masters_menu", "trans_menu", "report_menu"]:
            if hasattr(self, menu):
                getattr(self, menu).dismiss()

        self.root.current = screen_name

    # ==================================================
    # REPORT ACTIONS
    # ==================================================
    def show_stock_report(self):
        data = self.report_controller.get_stock()
        output = ""
        for i in data:
            output += f"{i.name} | Stock: {i.stock}\n"

        self.root.get_screen("reports").ids.report_output.text = output

    def show_outstanding_report(self):
        data = self.report_controller.get_outstanding()
        output = ""
        for l in data:
            output += f"Party {l.party_id} | Dr:{l.debit} Cr:{l.credit}\n"

        self.root.get_screen("reports").ids.report_output.text = output


ERPApp().run()
