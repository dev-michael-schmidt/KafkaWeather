import os
from typing import Callable, Iterable

from config import Configuration


def consumer_source(consumer):
    for msg in consumer:
        yield msg.value


def dispatch(source: Iterable[dict], handler: Callable[[dict], None], log=None):
    for msg in source:
        if log:
            log(f"Handling: {msg}")
        handler(msg)


class KafkaBase:
    def __init__(self, cfg: Configuration, role: str):

        bootstrap = os.getenv("KAFKA_BOOTSTRAP_SERVERS",
                              cfg.app.bootstrap_servers)   # fallback to YAML
        self.bootstrap_servers = bootstrap.split(",")
        self.topic = cfg.app.topic
        self.role = role

    def log(self, msg):
        print(f"[{self.role.upper()}] {msg}")
