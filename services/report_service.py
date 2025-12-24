
from repositories.item_repo import ItemRepository
from repositories.ledger_repo import LedgerRepository
class ReportService:
    def __init__(self):
        self.i=ItemRepository(); self.l=LedgerRepository()
    def stock(self): return self.i.all()
    def ledger(self): return self.l.all()
