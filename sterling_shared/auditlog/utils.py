import os
import logging
import requests 
import re
import jwt
import datetime
from .auditlog_data import AuditLogData
import decimal
import json
from uuid import UUID
from django.db.models import Model


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        if isinstance(o, datetime.date):
            return str(o)
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, UUID):
            return str(o)
        if isinstance(o, Model) and hasattr(o, 'to_dict'):
            return o.to_dict()
        if hasattr(o, 'name'):
            return str(o.name)
        if hasattr(o, 'id'):
            return str(o.id)
        return super().default(o)


def jsonize(data):
    return str(json.dumps(data, cls=CustomJsonEncoder))




def extract_browser_name(user_agent):
    browser_patterns = {
        'Chrome': 'Chrome\/[\d.]+',
        'Firefox': 'Firefox\/[\d.]+',
        'Safari': 'Version\/[\d.]+.*Safari',
        'Edge': 'Edge\/[\d.]+',
        'IE': 'Trident\/[\d.]+',
        'Opera': 'Opera\/[\d.]+',
    }
    for browser_name, pattern in browser_patterns.items():
        match = re.search(pattern, user_agent)
        if match:
            return browser_name
    return 'Unknown'


def get_module_id(module):
    module_map = {
        "User And Role Management": "user-role-mgt",
        "Currency": "currency-mgt",
        "Fiscal Period": "fiscal-period",
        "Segregation Of Duties": "seg-of-duties",
        "Security Configuration": "security-config"
    }
    return module_map[module]
    
logger_url = os.getenv("LOGGER_URL")
logger = logging.getLogger(__name__)


def create_log(endpoint_name, token_key, meta, user_request, action_type, action, microservice_name, module, old_value_json, new_value_json, affected_columns, session_id):
    decoded_token = jwt.decode(token_key, options={"verify_signature": False})
    role_ids = ", ".join(str(role_id) for role_id in decoded_token.get("role_ids", ""))
    role_names = ", ".join(str(role_name) for role_name in decoded_token.get("role_names", ""))
    fullname = f"{user_request.firstname} {user_request.lastname}"
    log_data = {
    "auditID": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
    "action": action,
    "sourceIP": meta.get('source_ip', 'Unknown'),
    "roleId": role_ids,
    "userActivityType": action_type,
    "microserviceName": microservice_name,
    "payloadCreatedDate": datetime.datetime.strptime(user_request.created_at, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%Y-%m-%d %H:%M:%S.%f"),
    "endpointName": endpoint_name,
    "oldValuesJson": old_value_json,
    "newValuesJson": new_value_json,
    "affectedColumns": affected_columns,
    "role": role_names,
    "userName": user_request.username if user_request.username else "",
    "fullName": fullname if fullname else "",
    "userID": str(getattr(user_request, 'id', '')),
    "createdDate": datetime.datetime.strptime(user_request.created_at, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%Y-%m-%d %H:%M:%S.%f"),
    "ipAddress": meta.get('ip_address', 'Unknown'),
    "startDate": datetime.datetime.strptime(user_request.created_at, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%Y-%m-%d %H:%M:%S.%f"),
    "endDate": datetime.datetime.strptime(user_request.created_at, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%Y-%m-%d %H:%M:%S.%f"),
    "branchCode": str(user_request.branch_code) if user_request.branch_code else "",
    "location": meta.get('ip_address', 'Unknown'),
    "branchName": user_request.branch if user_request.branch else "",
    "clientInfo": extract_browser_name(meta.get('user_agent', '')),
    "actionStatus": extract_browser_name(meta.get('user_agent', '')),
    "lastLogin": datetime.datetime.strptime(user_request.last_login, "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%Y-%m-%d %H:%M:%S.%f"),
    "sessionID": session_id,
    "module": module,
    "moduleID": get_module_id(module),
    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "productId": "",
    "productType": "",
    "productName": "",
    "reasonForFailure": "",
    "otherInformation": "",
    "authorizationDetails": "",
    "ledgerId": "",
    "ledgerName": "",
    "ledgerType": "",
    "ledgerClass": "",
    "customerId": "",
    "customerType": "",
    "customerName": "",
    "journalEntryInformation": "",
    "transactionValue": "",
    "exchangeRate": "",
    "debitAccounts": "",
    "creditAccounts": "",
    "chargeCode": "",
    "chargeName": "",
    "taxCode": "",
    "taxName": "",
    "recordId": "",
    "recordName": "",
    "transactionEntryInformation": "",
    "customerMandateView": "",
    "modifiedParameter": "",
    "periodCode": "",
    "currencyCode": "",
    "auditModuleAccessed": "",
    "investmentEntryInformation": "",
    "investmentProduct": "",
    "investmentAmount": "",
    "debitAccountLedger": "",
    "creditAccountLedger": "",
    "loanEntryInformation": "",
    "loanProduct": "",
    "loanAmount": "",
    "eocRunInformation": "",
    "eocRunLog": ""
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": token_key
    }
    try:
        response = requests.post(url=logger_url, headers=headers, json=log_data)
        response.raise_for_status()
    except Exception as e:
        print("sterling_shared.create_log",
              f"An error occurred while making API call: {e}")


def push_audit_log(data: AuditLogData):
    token = os.getenv("AUDITLOG_AUTH_TOKEN", data.sessionID)
    timeout = int(os.getenv("AUDITLOG_TIMEOUT", "5"))
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    try:
        print("sterling_shared.push_audit_log", data.to_dict())
        response = requests.post(
            url=logger_url,
            headers=headers,
            json=data.to_dict(),
            verify=False,
            timeout=timeout
        )
        print(
            "sterling_shared.push_audit_log",
            response.status_code,
            response.text
        )
        #response.raise_for_status()
        return response.text
    except Exception as e:
        print(
            "sterling_shared.push_audit_log",
            f"An error occurred while making API call: {e}"
        )
        return f"An error occurred while making API call: {e}"
