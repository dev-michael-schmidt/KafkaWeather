from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

BROKERS = ['broker-1:19092', 'broker-2:19092', 'broker-3:19092']

try:
    print(f"🧪 Connecting to Kafka brokers: {BROKERS}")
    consumer = KafkaConsumer(bootstrap_servers=BROKERS)
    topics = consumer.topics()
    print(f"✅ Connected! Available topics: {topics}")
    consumer.close()
except NoBrokersAvailable as e:
    print("❌ No brokers available:", e)
except Exception as e:
    print("❌ Unexpected error:", e)