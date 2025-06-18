import json
import time
from typing import Callable

from kafka import KafkaProducer

from src.config import Configuration
from src.kafka_base import KafkaBase


class KafkaProducerApp(KafkaBase):
    def __init__(self, cfg):
        super().__init__(cfg, role='producer')
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send(self, message: dict):
        self.log(f"Sending: {message}")
        self.producer.send(self.topic, value=message)
        self.producer.flush()

    def run(self, message_factory: Callable[[], dict], interval_seconds=10):
        self.run_loop(
            source=message_factory,
            handler=self.send,
            interval_seconds=interval_seconds,
            log=self.log
        )
