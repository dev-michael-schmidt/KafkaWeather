import json
from kafka import KafkaProducer

from kafka_base import KafkaBase, dispatch, producer_source


class KafkaProducerApp(KafkaBase):
    def __init__(self, cfg):
        super().__init__(cfg, role='producer')
        self.cfg = cfg
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send(self, message: dict):
        self.log(f"Sending: {message}")
        self.producer.send(self.topic, value=message)
        self.producer.flush()

    def run(self):
        dispatch(
            source=producer_source(self.cfg),
            handler=self.send,
            log=self.log
        )
