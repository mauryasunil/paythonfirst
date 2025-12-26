
from database import Session
from models.item import Item

def add_item(item):
    s = Session()
    s.add(item)
    s.commit()
    s.close()

def get_items():
    s = Session()
    r = s.query(Item).all()
    s.close()
    return r
