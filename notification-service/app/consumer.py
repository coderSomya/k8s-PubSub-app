from kafka import KafkaConsumer
import json
from email_sender import send_email

NOTIFICATION_TOPIC = 'notification'

consumer = KafkaConsumer(
        NOTIFICATION_TOPIC,
        bootstrap_servers = 'kafka:9092',
        value_deserializer = lambda m: json.loads(m.decode('utf-8'))
)

def consume_notifications():
    for message in consumer:
        order = message.value
        send_email(order)
