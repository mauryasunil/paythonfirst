
from database import SessionLocal
from models.item import Item


class ItemRepository:

   def add_item(item):
    s = SessionLocal()
    s.add(item)
    s.commit()
    s.close()

   def get_items():
    s = SessionLocal()
    r = s.query(Item).all()
    s.close()
    return r
