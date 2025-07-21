import time

from config import Configuration
from telegram import push_message
from kafka_consumer import KafkaConsumerApp


def handle_incoming_message(message: dict):
    print(f"📩 Got message: {message}")

def main():
    cfg = Configuration.from_yaml()


    KafkaConsumerApp(cfg).run(lambda d: push_message("msg", '42', cfg))
    # else:
    # KafkaProducerApp(cfg).run(lambda d: get_weather(cfg))



if __name__ == "__main__":
    main()
