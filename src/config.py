import yaml


class Config:
    def __init__(self, path='config.yaml'):
        self.path = path
        with open(self.path, "r") as f:
            self.config = yaml.safe_load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)




