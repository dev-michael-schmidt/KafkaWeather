import time

from src.config import Configuration
from src.telegram import push_message
from src.weather import get_weather
from src.kafka_consumer import KafkaConsumerApp
from src.kafka_producer import KafkaProducerApp


def handle_incoming_message(message: dict):
    print(f"📩 Got message: {message}")


def main():
    # Start consumer thread
    threading.Thread(target=consumer_loop, daemon=True).start()

    while True:
        print("⏳ Checking weather...")
        try:
            weather = get_weather(LAT, LON)
            code = weather["weathercode"]
            summary = weathercode_map.get(code, "Unknown")
            print(f"📡 Current weather: {summary} ({code})")

            if is_bad_weather(code):
                alert = f"Bad weather: {summary} at {weather['time']}"
                print(f"🚨 Sending alert: {alert}")
                send_weather_alert(alert)
            else:
                print("✅ Weather is fine.")

        except Exception as e:
            print(f"⚠️ Error: {e}")

        time.sleep(3600)  # Wait an hour before next check




def main():





if __name__ == '__main__':
    main()