from services.item_service import ItemService

class ItemController:

    def __init__(self):
        self.service = ItemService()

    def save_item(self, data):
        return self.service.create_item(data)

    def get_items(self):
        return self.service.fetch_items()
