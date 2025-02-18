import os
from shared_utils.services.base import BaseRequest


class AccountingService(BaseRequest):
    base_url = f"{os.getenv('ACCOUNTING_SERVICE_URL', 'http://localhost:10060')}/api/v1"
