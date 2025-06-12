from configparser import ConfigParser

from kafka import KafkaConsumer


from src.config import Config

cfg = Config()
app = cfg.get('app')

def deliver_weather():

    # Create a Kafka consumer
    consumer = KafkaConsumer(
        app.get('topic'),
        bootstrap_servers=app.get('bootstrap_servers'),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda m: m.decode('utf-8')  # Decode bytes to string
    )

    for message in consumer:
        print(f"[{message.partition}:{message.offset}] {message.value}")
