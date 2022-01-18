# Twitter contest enterer

This program is a twitter bot that participates in giveaways.
It can work in multiple language, can retweet, like, follow users, tag friends, and comment wrypto wallet address.
This program can be used with command line argument to be easily scheluded with crontab.

## Installation

Linux Debian/Ubuntu/Mint:

```bash
git clone 
cd twitter_giveaway_enterer
mv config_example.json config.json
# make sure to have pip install
pip3 install tweepy
```

## Configuration

This program requires a twitter developer account to access the twitter api.  
Check out this page if you don't have one yet https://developer.twitter.com/en  
Once you have an account create an app and generate your token.  
You are now ready to fill the configuration file.

| key           |     description |
| ------------- |  -------------: |
|   bearer_token   |    Your bearer token from twitter           |
| consumer_key     |        Your consumer key from twitter      |
| consumer_secret      |     Your consumer secret from twitter          |
| access_key      |       Your access key from twitter        |
| access_secret      |         Your access secret from twitter      |
| banned_users      |      The name of the users you want to be be ignored by the program         |
| banned_words      |      the words you want to ignore. Basically words like youtube or telegram because it would be giveaway that requires a not doable action        |
| research      |     A dictionnary where the key is language and the value the keyword for the tweet research. Ex: "en" : "giveaway"          |
| tag_sentences      |     A list of sentences that you want to be used when you mention friends          |
| tag_users      |       A list of users that will be used randomly when it's required to tag friends. AT least 5 is recommended     |
| sol_address      |       Your solana addresse that will be replied to the tweet if required. Can be an empty string 
| eth_address      |       Your ethereum addresse that will be replied to the tweet if required. Can be an empty string     |

## Run

To run the program use the following command line:  
`python3 main.py <language>`  
By default it supports english and french language:
```bash
# The language argument is defined is the configuration file. Any language can be added
python3 main.py en
python3 main.py fr
```