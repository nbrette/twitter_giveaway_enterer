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
pip3 install emoji
```

## Configuration

This program requires a twitter developer account to access the twitter api.  
Check out this page if you don't have one yet https://developer.twitter.com/en  
Once you have an account create an app and generate your token.  
You are now ready to fill the configuration file.

| key           |     description |
| ------------- |  -------------: |
|   bearer_token   |    List of your bearer tokens from twitter           |
| consumer_key     |        List of your consumer keys from twitter      |
| consumer_secret      |     List of your consumer secrets from twitter          |
| access_key      |       List of your access keys from twitter        |
| access_secret      |         List of your access secrets from twitter      |
| banned_users      |      The name of the users you want to be be ignored by the program         |
| banned_words      |      the words you want to ignore. Basically words like youtube or telegram because it would be giveaway that requires a not doable action        |
| research      |     A dictionnary where the key is language and the value the keyword for the tweet research. Ex: "en" : "giveaway"          |
| tag_sentences      |     A list of sentences that you want to be used when you mention friends          |
| tag_users      |       A list of users that will be used randomly when it's required to tag friends. At least 5 is recommended     |
| sol_address      |       Your solana addresse that will be replied to the tweet if required. Can be an empty string 
| eth_address      |       Your ethereum addresse that will be replied to the tweet if required. Can be an empty string     |

Although you can put multiple tokens to use multiple accounts, be aware that this feature is not implemented yet. The first account of the list will be used.  

## Run

To run the program use the following command line:  
`python3 main.py <language>`  
By default it supports english and french language:
```bash
# The language argument is defined is the configuration file. Any language can be added
python3 main.py en
python3 main.py fr
```

## Potential malfunction

You may notice that sometimes a tweet has only been retweeted and not liked for example. This is because twitter server can be over capacity and requests return an error so every action requested to enter the giveaway have not been performed.  
The error is handled and the program is gonna keep going if that happens but there is no way to avoid that.  
However it happens pretty rarely and it can change from one second to the other.