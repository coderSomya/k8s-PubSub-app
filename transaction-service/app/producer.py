from kafka import KafkaProducer
import json

producer_analytics = KafkaProducer(
        bootstrap_servers = 'kafka:9092',
        value_serializer= lambda v: json.dumps(v).encode('utf-8')
)

producer_notification = KafkaProducer(
        bootstrap_servers = 'kafka:9092',
        value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

NOTIFICATION_TOPIC ='notification'
ANALYTICS_TOPIC = 'analytics'

def produce_analytics(order):
    producer_analytics.send(ANALYTICS_TOPIC, order)
    producer_analytics.flush()

def produce_notification(order):
    producer_notification.send(NOTIFICATION_TOPIC, order)
    producer_notification.flush()

