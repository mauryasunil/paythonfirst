from database import SessionLocal
from models.item_master import Item

class ItemRepository:

    def add_item(self, data):
        db = SessionLocal()
        item = Item(**data)
        db.add(item)
        db.commit()
        db.refresh(item)
        db.close()
        return item

    def get_all(self):
        db = SessionLocal()
        items = db.query(Item).all()
        db.close()
        return items
