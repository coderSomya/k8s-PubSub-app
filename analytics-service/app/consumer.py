from kafka import KafkaConsumer
import json

ANALYTICS_TOPIC = 'analytics'

consumer = KafkaConsumer(
        ANALYTICS_TOPIC,
        bootstrap_servers = 'kafka:9092',
        value_deserializer = lambda m: json.loads(m.decode('utf-8'))
)

def consume_analytics():
    for message in consumer:
        order = message.value
        print("analytics received an order: {order}")

        # perform some analytics

