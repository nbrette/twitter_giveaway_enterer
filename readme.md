# Twitter contest enterer

This program is a twitter bot that participates in giveaways.
It can work in multiple languages, can retweet, like, follow users, tag friends, and comment crypto wallet address.  
This program can be used with command line argument to be easily scheluded with crontab.  
The accuracy of the bot  is currently over 90% however be aware that a lot of specific case can be encountered depending on how the give away tweet is written.

## Installation

Linux Debian/Ubuntu/Mint:

```bash
git clone https://github.com/nbrette/twitter_giveaway_enterer.git
cd twitter_giveaway_enterer
mv config_example.json config.json
# make sure to have pip install
pip3 install tweepy
pip3 install emoji
```

## Configuration

This program requires a twitter developer account to access the twitter api.  
Check out this page if you don't have one yet :  
https://developer.twitter.com/en  
Once you have an account create an app and generate your token.  
You are now ready to fill the configuration file.

| key           |     description |
| ------------- |  -------------: |
| banned_users      |      The name of the users you want to be be ignored by the program  - FEATURE NOT IMPLEMENTED YET       |
| banned_words      |      the words you want to ignore. Basically words like youtube or telegram because it would be giveaway that requires a not doable action        |
| research      |     A dictionnary where the key is language and the value the keyword for the tweet research. Ex: "en" : "giveaway"          |
| tag_sentences      |     A list of sentences that you want to be used when you mention friends          |
| tag_users      |       A list of users that will be used randomly when it's required to tag friends. At least 5 is recommended     |
| sol_address      |       Your solana addresse that will be replied to the tweet if required. Can be an empty string 
| eth_address      |       Your ethereum addresse that will be replied to the tweet if required. Can be an empty string     |
|credentials       | A dictionnary containing multiple dictionnaries. Each one represent a set of credentials for a twitter api app. Each dictionnary must contain the following keys: `bearer_token`, `consumer_key`,`consumer_secret`,`access_key` and `access_secret`|



## Run

To run the program use the following command line:  
`python3 main.py <language>`  
By default it supports english and french language:
```bash
# The language argument is defined is the configuration file. Any language can be added
python3 main.py --language en --key bernardinho
python3 main.py --language fr --key bernardinho
```

## Potential malfunction

### Twitter API Limit
Be aware that twitter api has different limits depending on the type of request.  
If you shedule this program to run regularly you should try to different intervals to see if your project get banned.  
Check this page to know more about twitter api limits:  
https://developer.twitter.com/en/docs/twitter-api/rate-limits

### Error "tag" not found
You may encounter the error "tag" not found sometimes. This is due to tweet containing the expression "-tag" with the hyphen.  
I have not found a work around yet.


