import time
from typing import Callable, Iterable

import requests

from config import Configuration


def get_weather(weather_config: Configuration) -> dict:

    params = {
        "latitude": weather_config.location.lat,
        "longitude": weather_config.location.long,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation",
        "timezone": "auto",
    }

    response = requests.get(weather_config.apis.weather_url, params=params)
    response.raise_for_status()
    data = response.json()
    return data


def producer_source(config):
    while True:
        yield get_weather(config)
        print('Sleeping...')
        time.sleep(3600)


def dispatch(source: Iterable[dict], handler: Callable[[dict], None], log=None):
    for msg in source:
        if log:
            log(f"Handling: {msg}")
        handler(msg)


class KafkaBase:
    def __init__(self, cfg: Configuration, role: str):
        # self.app = cfg.app
        self.bootstrap_servers = cfg.app.bootstrap_servers
        self.topic = cfg.app.topic
        self.role = role

    def log(self, msg):
        print(f"[{self.role.upper()}] {msg}")
