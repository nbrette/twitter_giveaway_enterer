from models.twitter_account_credentials import TwitterAccountCredentials
from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    credentials : TwitterAccountCredentials
    banned_words : List
    eth_address : str
    sol_address : str
    sentences : List
    usernames : List


