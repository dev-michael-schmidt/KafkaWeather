import json
from typing import Callable

from kafka import KafkaConsumer

from config import Configuration
from kafka_base import KafkaBase


class KafkaConsumerApp(KafkaBase):
    def __init__(self, cfg: Configuration):
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
        self.dispatch(
            handler=handle_message,
            log=self.log
        )
