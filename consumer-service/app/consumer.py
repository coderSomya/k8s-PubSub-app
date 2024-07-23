from kafka import KafkaConsumer
import json
import requests

KAFKA_TOPIC = 'orders'

consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers = 'kafka:9092',
        value_deserializer = lambda m: json.loads(m.decode('utf-8'))
        )

def consume_orders():
    for message in consumer:
        order = message.value
        requests.post('http://transaction-service:5000/transaction', json=order)
