import json
from typing import Callable

from kafka import KafkaConsumer

from src.config import AppConfig
from src.kafka_base import KafkaBase


class KafkaConsumerApp(KafkaBase):
    def __init__(self, cfg: AppConfig):
        super().__init__(cfg, role='consumer')
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

    def run(self, handle_message: Callable[[dict], None]):
        self.run_loop(
            source=self.consumer,
            handler=handle_message,
            log=self.log
        )