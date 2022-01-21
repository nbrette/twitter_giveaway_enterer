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
KEY_INDEX = "key_index"
RUN_FILE_PATH = "run_file/run.json"


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


def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)

def get_key_index():
    with open(RUN_FILE_PATH) as file:
        data = json.load(file)
        return data[KEY_INDEX]

def update_key_index(value):
    with open(RUN_FILE_PATH, 'w') as outfile:
        json.dump({KEY_INDEX : value}, outfile)

