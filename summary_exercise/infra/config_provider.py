import json


class ConfigProvider:

    @staticmethod
    def load_from_file():
        try:
            with open('../config.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {file} not found. Starting with an empty library.")