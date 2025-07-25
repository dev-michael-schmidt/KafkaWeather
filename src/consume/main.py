import os

from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

from config import Configuration

from consumer import KafkaConsumerApp, handle_message


def main():
    cfg = Configuration.from_yaml()
    KafkaConsumerApp(cfg).run(handle_message=handle_message)


if __name__ == "__main__":

    BROKERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS')
    print(f"🧪 Connecting to Kafka brokers: {BROKERS}")

    try:
        consumer = KafkaConsumer(bootstrap_servers=BROKERS)

        topics = consumer.topics()
        print(f"✅ Connected! Available topics: {topics}")

        consumer.close()
    except NoBrokersAvailable as e:
        print("❌ No brokers available:", e)
    except Exception as e:
        print("❌ Unexpected error:", e)

    main()