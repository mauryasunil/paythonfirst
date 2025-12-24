
from repositories.ledger_repo import LedgerRepository
from models.ledger import Ledger
class KhataService:
    def __init__(self): self.repo=LedgerRepository()
    def debit(self,p,a,n): self.repo.add(Ledger(party_id=p,debit=a,narration=n))
    def credit(self,p,a,n): self.repo.add(Ledger(party_id=p,credit=a,narration=n))
