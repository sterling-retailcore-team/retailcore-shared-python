import os
import logging
import requests 
import re
import jwt
import datetime


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


logger_url = os.getenv("LOGGER_URL")
logger = logging.getLogger(__name__)

def create_log(endpoint_name, token_key, meta, user_request, action_type, action, microservice_name, module, module_id, old_value_json, new_value_json, affected_columns):
    decoded_token = jwt.decode(token_key, options={"verify_signature": False})
    role_ids = ", ".join(str(role_id) for role_id in decoded_token.get("role_ids", ""))
    role_names = ", ".join(str(role_name) for role_name in decoded_token.get("role_names", ""))
    log_data = {
    "action": action,
    "sourceIP": meta.get('source_ip', 'Unknown'),
    "roleId": role_ids,
    "userActivityType": action_type,
    "microserviceName": microservice_name,
    "payloadCreatedDate": user_request.created_at.strftime("%Y-%m-%d %H:%M:%S") if isinstance(user_request.created_at, datetime.datetime) else "",
    "endpointName": endpoint_name,
    "oldValuesJson": old_value_json,
    "newValuesJson": new_value_json,
    "affectedColumns": affected_columns,
    "role": role_names,
    "userName": getattr(user_request, 'username', ''),
    "fullName": f"{getattr(user_request, 'firstname', '')} {getattr(user_request, 'lastname', '')}",
    "userID": str(getattr(user_request, 'id', '')),
    "createdDate": user_request.created_at.strftime("%Y-%m-%d %H:%M:%S") if isinstance(user_request.created_at, datetime.datetime) else "",
    "ipAddress": meta.get('ip_address', 'Unknown'),
    "startDate": user_request.created_at.strftime("%Y-%m-%d %H:%M:%S") if isinstance(user_request.created_at, datetime.datetime) else "",
    "endDate": user_request.created_at.strftime("%Y-%m-%d %H:%M:%S") if isinstance(user_request.created_at, datetime.datetime) else "",
    "branchCode": getattr(user_request, 'branch_code', ''),
    "location": meta.get('ip_address', 'Unknown'),
    "branchName": getattr(user_request, 'branch', ''),
    "clientInfo": extract_browser_name(meta.get('user_agent', '')),
    "actionStatus": extract_browser_name(meta.get('user_agent', '')),
    "lastLogin": user_request.last_login.strftime("%Y-%m-%d %H:%M:%S") if isinstance(user_request.last_login, datetime.datetime) else "",
    "sessionID": microservice_name,
    "module": module,
    "fullname": f"{getattr(user_request, 'firstname', '')} {getattr(user_request, 'lastname', '')}",
    "moduleID": module_id,
    "timestamp": user_request.created_at.strftime("%Y-%m-%d %H:%M:%S") if isinstance(user_request.created_at, datetime.datetime) else "",
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": token_key
    }
    try:
        response = requests.post(url=logger_url, headers=headers, json=log_data)
        response.raise_for_status()
    except Exception as e:
        logger.error(f"An error occurred while making API call: {e}")
