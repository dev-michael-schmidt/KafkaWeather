import requests

from src.config import Configuration
from weather_code_map import WeatherCodeMap


def get_weather(weather_config: Configuration) -> dict:

    params = {
        "latitude": weather_config.location.lat,
        "longitude": weather_config.location.long,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation",
        "timezone": "auto",
    }

    response = requests.get(weather_config.apis.weather_url, params=params)
    response.raise_for_status()
    data = response.json()

    weather_code = data['current_weather']['weathercode']
    name = weather_config.location.name
    if weather_code in WeatherCodeMap.rain_codes:
        data['result'] = f"it's raining in {name}"
    elif weather_code in WeatherCodeMap.snow_codes:
        data['result'] = f"it's snowing in {name}"
    elif weather_code in WeatherCodeMap.bad_weather:
        data['result'] = f"it's bad in {name}"
    else:
        data['result'] = f"No precipitation in {name}"

        if weather_code in bad_weather:
            return f"it's bad weather in {name}"

        return f"No precipitation in {name}"
