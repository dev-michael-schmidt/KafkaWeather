from kafka import KafkaProducer

from src.config import Config
from src.open_meteo import get_weather

cfg = Config()
app = cfg.get('app')

def produce_weather():
    producer = KafkaProducer(
        bootstrap_servers=app.get('bootstrap_servers'),
        value_serializer=lambda v: v.encode('utf-8')  # Convert string to bytes
    )

    topic = app.get('topic')
    message = get_weather()

    producer.send(topic, value=message)
    producer.flush()
