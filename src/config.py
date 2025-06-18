from dataclasses import dataclass

import yaml


@dataclass(frozen=True)
class AppConfig:
    bootstrap_servers: str
    topic: str
    name: str

@dataclass(frozen=True)
class ApisConfig:
    weather_url: str
    telegram_url_template: str
    telegram_bot_token: str

@dataclass(frozen=True)
class LocationConfig:
    lat: float
    long: float
    name: str

@dataclass(frozen=True)
class Configuration:
    app: AppConfig
    apis: ApisConfig
    location: LocationConfig

    @staticmethod
    def from_yaml(path: str = 'app_config.yaml') -> "Configuration":
        with open(path, "r") as f:
            raw = yaml.safe_load(f)

        return Configuration(
            app=AppConfig(**raw['app']),
            apis=ApisConfig(**raw['apis']),
            location=LocationConfig(**raw['location']),
        )
