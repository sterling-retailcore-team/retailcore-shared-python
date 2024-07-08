import os
from django.conf import settings
from kafka import KafkaProducer
from sterling_shared.auditlog.utils import jsonize


producer = KafkaProducer(
    bootstrap_servers = os.getenv("KAFKA_SERVER"),
    value_serializer=lambda v: jsonize(v, to_string=True).encode('utf-8')
)

def push_to_background(action: str, data=None):
    try:
        producer.send(os.getenv("KAFKA_TOPIC"), dict(action=action, data=data))
        producer.flush()
    except Exception as ex:
        print("!!!!!CRITICAL!!!!")
        print("!!!!!KAFKA IS FAILING!!!!")
        print("push_to_background", ex)