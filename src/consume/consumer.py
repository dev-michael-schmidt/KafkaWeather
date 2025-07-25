import os
import json
from typing import Callable

from kafka import KafkaConsumer

from config import Configuration
from kafka_base import consumer_source, dispatch, KafkaBase
from weather_code_map import rain_codes, snow_codes, bad_weather
from send_gmail import send_gmail


def handle_message(message: dict):
    print(f'Sending gmail/sms message!')

    weather_code = message['current_weather']['weathercode']
    print(f'weather code: {weather_code}')

    if weather_code in RAIN_CODES:
        result = "it's raining"
    elif weather_code in SNOW_CODES:
        result = "it's snowing"
    elif weather_code in SEVERE_WEATHER:
        result = "it's bad out there"
    else:
        result = "It's a nice day"

    print(f'result: {result}')

    send_gmail(subject='weather update',
               body=result,
               to_addr=os.environ['TO_ADDR'],
               from_addr=os.environ['GMAIL_USER'],
               app_password=os.environ['GMAIL_APP_PASS'])


class KafkaConsumerApp(KafkaBase):
    def __init__(self, cfg: Configuration):
        super().__init__(cfg, role='consumer')

        group_id = os.environ['KAFKA_GROUP_ID']

        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

    def run(self, handle_message: Callable[[dict], None]):
        dispatch(consumer_source(self.consumer), handler=handle_message, log=self.log)
