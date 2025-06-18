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


    def get_producer(self):

    params = {
        "latitude": weather_config.location.lat,
        "longitude": weather_config.location.long,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation",
        "timezone": "auto",
    }

        response = requests.get(self.apis.get('weather_url'), params=params)
        response.raise_for_status()  # Raises error for HTTP failures
        data = response.json()

    weather_code = data['current_weather']['weathercode']
    name = weather_config.location.name
    if weather_code in WeatherCodeMap.rain_codes:
        data['result'] = f"it's raining in {name}"
    elif weather_code in WeatherCodeMap.snow_codes:
        data['result'] = f"it's snowing in {name}"
    elif weather_code in WeatherCodeMap.bad_weather:
        data['result'] = f"it's bad in {name}"
    else:
        data['result'] = f"No precipitation in {name}"

        if weather_code in bad_weather:
            return f"it's bad weather in {name}"

        return f"No precipitation in {name}"
