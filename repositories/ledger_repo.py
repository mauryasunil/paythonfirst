
from database import SessionLocal
from models.ledger import Ledger
class LedgerRepository:
    def add(self,l):
        s=Session(); s.add(l); s.commit(); s.close()
    def all(self):
        s=Session(); r=s.query(Ledger).all(); s.close(); return r
