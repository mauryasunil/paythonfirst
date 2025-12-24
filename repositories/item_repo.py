
from database import SessionLocal
from models.item import Item
class ItemRepository:
    def add(self,item):
        s=Session(); s.add(item); s.commit(); s.close()
    def all(self):
        s=Session(); r=s.query(Item).all(); s.close(); return r
