
from services.inventory_service import InventoryService
class ItemController:
    def __init__(self): self.s=InventoryService()
    def save(self,name): self.s.add_item(name)
