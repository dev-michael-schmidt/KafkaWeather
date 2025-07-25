from config import Configuration
from kafka_producer import KafkaProducerApp


def main():
    cfg = Configuration.from_yaml()
    KafkaProducerApp(cfg).run()


if __name__ == "__main__":
    main()
