
from repositories.item_repo import ItemRepository
from models.item import Item
class InventoryService:
    def __init__(self): self.repo=ItemRepository()
    def add_item(self,name):
        self.repo.add(Item(name=name))
    def get_stock(self): return self.repo.all()
