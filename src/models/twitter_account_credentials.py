from dataclasses import dataclass

@dataclass
class TwitterAccountCredentials:
    bearer_token: str
    access_key: str
    access_secret: str
    consumer_key: str
    consumer_secret: str