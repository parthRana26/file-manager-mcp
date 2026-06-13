import os

API_KEY = os.getenv("API_KEY")


def verify_api_key(api_key: str):
    if api_key != API_KEY:
        raise ValueError(
            "Invalid API Key"
        )