import requests

from src import config
from src.config import Config


class TelegramNotifier:
    def __init__(self, chat_id):
        self.config = Config()
        self.apis = config.get('apis')
        self.bot_token = config.get('telegram_bot_token')
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{self.apis.get('telegram_bot_token')}"

    def send_message(self, msg: str) -> bool:
        payload = {
            "chat_id": self.chat_id,
            "text": msg,
            "parse_mode": "Markdown",
        }
        try:
            response = requests.post(f'{self.api_url}/sendMessage', json=payload, timeout=10)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Error sending message: {e}")
            return False
