from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from controllers.customer_controller import CustomerController

class CustomerScreen(MDScreen):

    def on_pre_enter(self):
        self.controller = CustomerController()
        self.load_customers()

    def save_customer(self):
        data = {
            "name": self.ids.name.text,
            "mobile": self.ids.mobile.text,
            "address": self.ids.address.text
        }

        self.controller.save_customer(data)
        self.clear_fields()
        self.load_customers()

    def load_customers(self):
        self.ids.customer_list.clear_widgets()
        for c in self.controller.fetch_customers():
            self.ids.customer_list.add_widget(
                OneLineListItem(
                    text=f"{c.name} | {c.mobile}"
                )
            )

    def clear_fields(self):
        self.ids.name.text = ""
        self.ids.mobile.text = ""
        self.ids.address.text = ""
