import os
import logging
import requests
import jwt
import re

from jwt.exceptions import InvalidTokenError, DecodeError


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

def create_log(request, action_type, action, microservice_name, module, module_id, oldvaluejson, newvaluejson, affected_columns):
    user_agent = request.META.get('HTTP_USER_AGENT', ' ')
    endpoint_name = request.path
    try:
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            message = "Authorization header is missing"
            logger.error(message)
            return message
        token_key = str(authorization_header.split(' ')[1])
        decoded_data = jwt.decode(token_key, options={"verify_signature": False})
        role_ids = ", ".join(str(role_id) for role_id in decoded_data["role_ids"])
        role_names = ", ".join(str(role_name) for role_name in decoded_data["role_names"])
    except (InvalidTokenError, DecodeError) as e:
        message = "Invalid token or decoding error"
        logger.warning(e)
        return message

    log_data = {
    "action": action,
    "sourceIP": request.META.get('REMOTE_ADDR', 'Unknown'),
    "roleId": role_ids,
    "userActivityType": action_type,
    "microserviceName": microservice_name,
    "payloadCreatedDate": str(getattr(request.user, 'created_at', '')) if getattr(request.user, 'created_at', '') else None,
    "endpointName": endpoint_name,
    "oldValuesJson": oldvaluejson,
    "newValuesJson": newvaluejson,
    "affectedColumns": affected_columns,
    "role": role_names,
    "userName": getattr(request.user, 'username', ''),
    "fullName": f"{getattr(request.user, 'firstname', '')} {getattr(request.user, 'lastname', '')}",
    "userID": str(getattr(request.user, 'id', '')),
    "createdDate": str(getattr(request.user, 'created_at', '')),
    "ipAddress": request.META.get('REMOTE_ADDR', 'Unknown'),
    "startDate": str(getattr(request.user, 'created_at', '')) if getattr(request.user, 'created_at', '') else None,
    "endDate": str(getattr(request.user, 'created_at', '')) if getattr(request.user, 'created_at', '') else None,
    "branchCode": getattr(request.user, 'branch_code', ''),
    "location": request.META.get('REMOTE_ADDR', 'Unknown'),
    "branchName": getattr(request.user, 'branch', ''),
    "clientInfo": extract_browser_name(user_agent),
    "actionStatus": getattr(request, 'status_code', None),
    "lastLogin": str(getattr(request.user, 'last_login', '')) if getattr(request.user, 'last_login', '') else None,
    "sessionID": microservice_name.title(),
    "module": module.title(),
    "fullname": f"{getattr(request.user, 'firstname', '')} {getattr(request.user, 'lastname', '')}",
    "moduleID": module_id,
    "timestamp": str(getattr(request.user, 'created_at', '')) if getattr(request.user, 'created_at', '') else None
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
