from core.celery import APP
from sterling_shared.auditlog.utils import create_log

@APP.task(serializer="pickle")
def send_activity_log(activity_data):
    create_log(
        activity_data["endpoint_name"],
        activity_data["token_key"],
        activity_data["meta"],
        activity_data["user_request"],
        activity_data["action_type"],
        activity_data["action"],
        activity_data["microservice_name"],
        activity_data["module"],
        activity_data["old_value_json"],
        activity_data["new_value_json"],
        activity_data["affected_columns"],
        activity_data["session_id"],

        )
