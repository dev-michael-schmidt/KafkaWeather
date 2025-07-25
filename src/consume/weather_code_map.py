from dataclasses import dataclass
from typing import ClassVar, Dict, Tuple

@dataclass(frozen=True)
class WeatherCodeMap:
    map: ClassVar[Dict[int, str]] = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm (slight or moderate)",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }

rain_codes = (51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82, 95, 96, 99)

snow_codes = (71, 73, 75, 77, 85, 86)

bad_weather = (65, 67, 75, 82, 95, 96, 99)
