import json
import re
import emoji

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
CREDENTIALS = "credentials"


def load_configfile(filename):
    with open(filename) as file:
        data = json.load(file)

        config = {
            BANNED_USERS: data[BANNED_USERS],
            BANNED_WORDS: data[BANNED_WORDS],
            RESEARCH : data[RESEARCH],
            TAG_SENTENCES : data[TAG_SENTENCES],
            TAG_USERS : data[TAG_USERS],
            SOL_ADDR : data[SOL_ADDR],
            ETH_ADDR : data[ETH_ADDR],
            CREDENTIALS : data[CREDENTIALS]
        }
    return config


def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)



