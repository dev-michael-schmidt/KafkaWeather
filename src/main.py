import time

from src.config import Configuration
from src.telegram import push_message
from src.weather import get_weather
from src.kafka_consumer import KafkaConsumerApp
from src.kafka_producer import KafkaProducerApp


def handle_incoming_message(message: dict):
    print(f"📩 Got message: {message}")


def main():
    cfg = Configuration.from_yaml()

    role = cfg.app
    if role == "producer":
        KafkaProducerApp(cfg).run(lambda: get_weather(cfg), interval_seconds=60)
    else:
        KafkaConsumerApp(cfg).run(lambda: push_message("msg", '42', cfg))


if __name__ == "__main__":
    main()
