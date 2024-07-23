from kafka import KafkaProducer
import json

KAFKA_TOPIC = 'orders'

producer = KafkaProducer(
    bootstrap_servers = 'kafka:9092',
    value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

def produce_order(order):
    producer.send(KAFKA_TOPIC, order)
    producer.flush()