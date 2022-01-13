import json
import re

BANNED_USERS = "banned_users"
BANNED_WORDS = "banned_words"
CONSUMER_KEY = "consumer_key"
CONSUMER_SECRET = "consumer_secret"
ACCESS_KEY = "access_key"
ACCESS_SECRET = "access_secret"
BEARER_TOKEN = "bearer_token"
RESEARCH = "research"
TAG_SENTENCES = "tag_sentences"
TAG_USERS = "tag_users"
SOL_ADDR = "sol_address"
ETH_ADDR = "eth_address"


def load_configfile(filename):
    with open(filename) as file:
        data = json.load(file)

        config = {
            BANNED_USERS: data[BANNED_USERS],
            BANNED_WORDS: data[BANNED_WORDS],
            CONSUMER_KEY: data[CONSUMER_KEY],
            CONSUMER_SECRET: data[CONSUMER_SECRET],
            ACCESS_KEY : data[ACCESS_KEY],
            ACCESS_SECRET : data[ACCESS_SECRET],
            BEARER_TOKEN : data[BEARER_TOKEN],
            RESEARCH : data[RESEARCH],
            TAG_SENTENCES : data[TAG_SENTENCES],
            TAG_USERS : data[TAG_USERS],
            SOL_ADDR : data[SOL_ADDR],
            ETH_ADDR : data[ETH_ADDR]
        }
    return config

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)