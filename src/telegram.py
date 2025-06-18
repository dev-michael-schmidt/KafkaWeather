import requests

from src.config import Configuration


def push_message(msg: str, chat_id: str, cfg: Configuration) -> bool:
    api_url = cfg.apis.telegram_url_template.format(
        bot_token=cfg.apis.telegram_bot_token)

    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "Markdown",
    }

    try:
        response = requests.post(f"{api_url}/sendMessage", json=payload, timeout=10)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Error sending message: {e}")
        return False
