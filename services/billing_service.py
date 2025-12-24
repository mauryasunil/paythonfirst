
from services.khata_service import KhataService
class BillingService:
    def __init__(self): self.khata=KhataService()
    def purchase(self,p,i,q,r):
        self.khata.credit(p,q*r,"Purchase")
