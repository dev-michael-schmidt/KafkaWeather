import requests

from src.config import Config
from src.weather_map import bad_weather, rain_codes, snow_codes


def get_weather():

    cfg = Config()

    loc = cfg.get('location')
    app = cfg.get('app')
    name = cfg.get('name', 'Area 51')

    params = {
        "latitude": loc.get('lat', 37.2350),
        "longitude": loc.get('long', -115.8111),
        "current_weather": True,
        "hourly": "temperature_2m,precipitation",
        "timezone": "auto",
    }

    response = requests.get(app.get('url'), params=params)
    response.raise_for_status()  # Raises error for HTTP failures
    data = response.json()

    weather_code = data['current_weather']['weathercode']
    if weather_code in rain_codes:
        return f"it's raining in {name}"

    if weather_code in snow_codes:
        return f"it's snowing in {name}"

    if weather_code in bad_weather:
        return f"it's bad weather in {name}"

    return f"No precipitation in {name}"



