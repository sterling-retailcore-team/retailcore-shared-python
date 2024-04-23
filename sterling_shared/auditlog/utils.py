import os
import requests
import settings

from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode

def create_log(request, action_type, action, microservice_name, module, module_id, oldvaluejson, newvaluejson, affected_columns: list):

    try:
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return
        token_key = str(authorization_header.split(' ')[1])
        UntypedToken(token_key)
    except (InvalidToken, TokenError) as e:
        return
    else:
        decoded_data = jwt_decode(token_key, settings.SECRET_KEY, algorithms=["HS256"])
        role_ids = decoded_data["role_ids"]
        role_names = decoded_data["role_names"]

    logger_url = os.getenv("LOGGER_URL")
    log_data = {
        "action": action,
        "roleid": role_ids,
        "useractivitytype": action_type,
        "microservicename": microservice_name,
        "endpointname": dict(request.headers),
        "oldvaluesjson": oldvaluejson,
        "newvaluesjson": newvaluejson,
        "affectedcolumns": affected_columns,
        "role": role_names,
        "firstname": request.user.firstname,
        "lastname": request.user.lastname,
        "username": request.user.username,
        "userid": str(request.user.id),
        "ipaddress": request.META.get('REMOTE_ADDR', 'Unknown'),
        "branchcode": request.user.branch_code,
        "branchname": request.user.branch,
        "actionstatus": None,
        "lastlogin": str(request.user.last_login) if request.user.last_login else None,
        "sessionid": "",
        "fullname": f"{request.user.firstname} {request.user.lastname}",
        "module": module,
        "moduleid": module_id,
        "timestamp": str(request.user.created_at) if request.user.created_at else None,
    }
    if hasattr(request, 'status_code'):
        log_data["actionstatus"] = request.status_code

    headers = {"Content-Type": "application/json",}
    try:
        requests.post(logger_url, headers=headers, json=log_data)
    except Exception as e:
        print(f"An error occurred while making API call: {e}")
