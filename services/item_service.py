from repositories.item_master_repo import ItemRepository

class ItemService:

    def __init__(self):
        self.repo = ItemRepository()

    def create_item(self, data):
        return self.repo.add_item(data)

    def fetch_items(self):
        return self.repo.get_all()
