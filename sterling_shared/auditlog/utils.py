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
    "useractivitytype": action_type,
    "roleid": role_ids,
    "role": role_names,
    "microservicename": microservice_name,
    "endpointname": dict(request.headers),
    "oldvaluesjson": oldvaluejson,
    "newvaluesjson": newvaluejson,
    "affectedcolumns": affected_columns,
    "firstname": getattr(request.user, 'firstname', ''),
    "lastname": getattr(request.user, 'lastname', ''),
    "username": getattr(request.user, 'username', ''),
    "userid": str(getattr(request.user, 'id', '')),
    "ipaddress": request.META.get('REMOTE_ADDR', 'Unknown'),
    "branchcode": getattr(request.user, 'branch_code', ''),
    "branchname": getattr(request.user, 'branch', ''),
    "actionstatus": getattr(request, 'status_code', None),
    "lastlogin": str(getattr(request.user, 'last_login', '')) if getattr(request.user, 'last_login', '') else None,
    "sessionid": "",
    "fullname": f"{getattr(request.user, 'firstname', '')} {getattr(request.user, 'lastname', '')}",
    "module": module,
    "moduleid": module_id,
    "timestamp": str(getattr(request.user, 'created_at', '')) if getattr(request.user, 'created_at', '') else None,
    }

    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(logger_url, headers=headers, json=log_data)
        response.raise_for_status()
    except Exception as e:
        logger.error(f"An error occurred while making API call: {e}")
        