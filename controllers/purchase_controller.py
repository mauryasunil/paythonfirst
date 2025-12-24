
from services.billing_service import BillingService
class PurchaseController:
    def __init__(self): self.s=BillingService()
    def save_purchase(self,p,i,q,r): self.s.purchase(int(p),int(i),float(q),float(r))
