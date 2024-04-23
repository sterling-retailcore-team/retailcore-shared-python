import os
import requests

def create_log(request, action_type, action, microservice_name, module, module_id, oldvaluejson, newvaluejson, affected_columns: list):
    logger_url = os.getenv("LOGGER_URL")
    log_data = {
        "action": action,
        "roleid": request.user.role_ids,
        "useractivitytype": action_type,
        "microservicename": microservice_name,
        "endpointname": dict(request.headers),
        "oldvaluesjson": oldvaluejson,
        "newvaluesjson": newvaluejson,
        "affectedcolumns": affected_columns,
        "role": request.user.role_names,
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