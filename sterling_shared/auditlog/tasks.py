from core.celery import APP
from auditlog.utils import create_log


@APP.task()
def send_activity_log(activity_data):
    create_log(
        activity_data["request"],
        activity_data["action_type"],
        activity_data["action"],
        activity_data["microservice_name"],
        activity_data["affected_columns"],
        activity_data["module"],
        activity_data["module_id"],
        activity_data["oldvaluejson"],
        activity_data["newvaluejson"],
    )
