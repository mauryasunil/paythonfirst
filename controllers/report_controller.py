
from services.report_service import ReportService
class ReportController:
    def __init__(self): self.s=ReportService()
    def get_stock(self): return self.s.stock()
    def get_outstanding(self): return self.s.ledger()
