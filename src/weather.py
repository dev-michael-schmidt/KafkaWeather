import requests
from kafka import KafkaConsumer, KafkaProducer
from src.config import Config
from src.weather_map import rain_codes, snow_codes, bad_weather


class Weather:

    def __init__(self):
        self.cfg = Config()
        self.app = self.cfg.get('app')
        self.apis = self.cfg.get('apis')
        self.location = self.cfg.get('location')

        self.consumer = self.get_consumer()

    def get_consumer(self):

        # Create a
        # Kafka consumer
        self.consumer = KafkaConsumer(
            self.app.get('topic'),
            bootstrap_servers=self.app.get('bootstrap_servers'),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda m: m.decode('utf-8')  # Decode bytes to string
        )
        return self.consumer

    def get_producer(self):

       producer = KafkaProducer(
            bootstrap_servers=self.app.get('bootstrap_servers'),
            value_serializer=lambda v: v.encode('utf-8')  # Convert string to bytes
        )
       topic = self.app.get('topic')
       message = self.get_weather()
       producer.send(topic, value=message)
       producer.flush()

    def get_weather(self):

        name = self.app.get('name', 'Area 51')
        params = {
            "latitude": self.location.get('lat', 37.2350),
            "longitude": self.location.get('long', -115.8111),
            "current_weather": True,
            "hourly": "temperature_2m,precipitation",
            "timezone": "auto",
        }

        response = requests.get(self.apis.get('weather_url'), params=params)
        response.raise_for_status()  # Raises error for HTTP failures
        data = response.json()

        weather_code = data['current_weather']['weathercode']
        if weather_code in rain_codes:
            return f"it's raining in {name}"

        if weather_code in snow_codes:
            return f"it's snowing in {name}"

        if weather_code in bad_weather:
            return f"it's bad weather in {name}"

        return f"No precipitation in {name}"
