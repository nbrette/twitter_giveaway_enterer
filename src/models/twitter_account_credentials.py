from dataclasses import dataclass
from typing import Optional

@dataclass
class TwitterAccountCredentials:
    bearer_token: str
    access_key: str
    access_secret: str
    consumer_key: str
    consumer_secret: str
    name : Optional[str] = None 
    