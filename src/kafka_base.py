import time
from typing import Callable, Iterable, Optional

from config import Configuration


class KafkaBase:
    def __init__(self, cfg: Configuration, role: str):
        # self.app = cfg.app
        self.bootstrap_servers = cfg.app.bootstrap_servers
        self.topic = cfg.app.topic
        self.role = role

    def log(self, msg):
        print(f"[{self.role.upper()}] {msg}")

    def dispatch(self, source: Callable[[], dict] | Iterable[dict],
                 handler: Callable[[dict], None],
                 interval_seconds: int = 1,
                 log: Optional[Callable[[str], None]] = None
                 ):
        def iter_messages():
            if callable(source):
                while True:
                    yield source()
                    time.sleep(interval_seconds)
            else:
                yield from source

        for msg in iter_messages():
            value = getattr(msg, "value", msg)
            if log:
                log(f"Handling: {value}")
            handler(value)

