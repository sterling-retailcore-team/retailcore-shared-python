import os
import logging
import requests
import jwt

from jwt.exceptions import InvalidTokenError, DecodeError


logger_url = os.getenv("LOGGER_URL")
logger = logging.getLogger(__name__)

def create_log(request, action_type, action, microservice_name, module, module_id, oldvaluejson, newvaluejson, affected_columns: list):
    try:
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            message = "Authorization header is missing"
            logger.error(message)
            return message
        token_key = str(authorization_header.split(' ')[1])
        decoded_data = jwt.decode(token_key, options={"verify_signature": False})
        role_ids = decoded_data["role_ids"]
        role_names = decoded_data["role_names"]
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
    "payloadCreatedDate": "",
    "endpointName": dict(request.headers),
    "oldValuesJson": oldvaluejson,
    "newValuesJson": newvaluejson,
    "affectedColumns": affected_columns,
    "role": role_names,
    "userName": getattr(request.user, 'username', ''),
    "fullName": f"{getattr(request.user, 'firstname', '')} {getattr(request.user, 'lastname', '')}",
    "userID": str(getattr(request.user, 'id', '')),
    "createdDate": str(getattr(request.user, 'created_at', '')),
    "ipAddress": request.META.get('REMOTE_ADDR', 'Unknown'),
    "startDate": "",
    "endDate": "",
    "branchCode": getattr(request.user, 'branch_code', ''),
    "location": "",
    "branchName": getattr(request.user, 'branch', ''),
    "clientInfo": "browsername",
    "actionStatus": getattr(request, 'status_code', None),
    "lastLogin": str(getattr(request.user, 'last_login', '')) if getattr(request.user, 'last_login', '') else None,
    "sessionID": "",
    "module": module,
    "fullname": f"{getattr(request.user, 'firstname', '')} {getattr(request.user, 'lastname', '')}",
    "moduleID": module_id,
    "timestamp": str(getattr(request.user, 'created_at', '')) if getattr(request.user, 'created_at', '') else None,
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
