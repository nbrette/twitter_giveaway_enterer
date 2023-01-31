from models.config import Config
from models.twitter_account_credentials import TwitterAccountCredentials
import tweepy
from services.utils import remove_emoji
import random
import logging
from typing import List
from tweepy.errors import Unauthorized, Forbidden, TooManyRequests

class TwitterController():
    def __init__(self, config : Config = None):

        if config is not None:
            self.client = tweepy.Client(config.credentials.bearer_token, config.credentials.consumer_key,
                                        config.credentials.consumer_secret, config.credentials.access_key, config.credentials.access_secret, wait_on_rate_limit=True)
            self.config = config
    
    def get_recent_tweets(self, research : str):
        giveaway_tweets = []
        research += " -is:retweet -is:reply"
        response = self.client.search_recent_tweets(
            query=research, max_results=100, tweet_fields=["entities", "created_at"], user_fields=['profile_image_url'], expansions=['author_id'])
        for tweet in response.data:
            tweet.text = tweet.text.lower()
            if self.check_is_contest(tweet.text):
                tweet.text = remove_emoji(tweet.text)
                giveaway_tweets.append(tweet)
        return giveaway_tweets
    
    def check_contains_bannedwords(self, tweet):
        contain = False
        for word in self.config.banned_words:
            if word in tweet.lower():
                contain = True
                break
        return contain
    
    def get_top_tweets(self, research : str):
        giveaway_tweets = []
        research += " -is:retweet -is:reply"
        response = self.client.search_recent_tweets(
            query=research, max_results=100, tweet_fields=["entities", "created_at"], user_fields=['profile_image_url'], expansions=['author_id'])
        for tweet in response.data:
            tweet.text = tweet.text.lower()
            if self.check_is_contest(tweet.text):
                tweet.text = remove_emoji(tweet.text)
                giveaway_tweets.append(tweet)
        return giveaway_tweets

    def check_is_contest(self, tweet : str):
        lower_tweet = tweet.lower()
        is_contest = False
        if (any(word in lower_tweet for word in ["rt", "retweet"])) and ("follow" in lower_tweet):
            is_contest = True
        return is_contest
    
    def get_mentionned_users(self, tweet):
        id_users = []
        if (tweet.entities != None and "mentions" in tweet.entities):
            users = tweet.entities["mentions"]
            for u in users:
                id_users.append(u["id"])
        return id_users

    def get_nb_of_friends_to_tag(self, tweet : str):
        """
        Find the number of friends that must be tagged
        If the tweet does not contain the word tag the number will be 0
        If the tweet contains the word tag than the tweet is split and the number found after the word 'tag' is considered the number of friends.
        However it does not make sense this number is greater than 5. If that's the case the number of friends to tag will be 3.
        """
        nb_of_friends = 0
        nb_of_friends_found = False

        if (("tag" in tweet)):
            # Check how many people must be tagged
            words = tweet.split()
            #If the word tag is written something like -tag it could create an error, in that case we just get 3 as the number of friends to tag
            try:
                index = words.index("tag")
            except ValueError:
                logging.warning('The word could not be found. Number of friends to tag is 3 by default')
                return 3
            words = words[index:]
            for word in words:
                if word.isdigit():
                    nb_of_friends = int(word)
                    nb_of_friends_found = True
                    break
            #If no number of friends found or if the number of friends does not make sense
            if (nb_of_friends_found == False) or (nb_of_friends > 5):
                nb_of_friends = 3

        return nb_of_friends
    
    def default_action(self, tweet):
        self.client.retweet(tweet.id)
        self.client.like(tweet.id)
        self.client.follow(tweet.author_id)

    def enter_giveaway(self, tweet):
        self.default_action(tweet)
        tweet_to_publish = random.choice(self.config.sentences)
        crypto_reply = self.check_crypto_address(tweet.text)
        if crypto_reply is not None:
            tweet_to_publish = crypto_reply

        
        #Get every user mentionned in the tweet and follow them
        mentionned_users = self.get_mentionned_users(tweet)
        for user in mentionned_users:
            self.client.follow(user)

        #Check if people must be tagged
        #If it is the case select random usernames and tag them in the comment
        nb_of_friends_to_tag = self.get_nb_of_friends_to_tag(tweet.text)
        if nb_of_friends_to_tag > 0:
            friends_usernames = random.choices(self.config.usernames,k=nb_of_friends_to_tag)
            for username in friends_usernames:
                tweet_to_publish += ' @'
                tweet_to_publish += username
        logging.debug(tweet_to_publish)
        self.client.create_tweet(text=tweet_to_publish, in_reply_to_tweet_id=tweet.id)
    
    def verify_credentials(self, credentials : List[TwitterAccountCredentials]):
        """
        Try to get a tweet to check if the credentials work
        """
        credentials_validity = {}
        
        for credential in credentials:
            try:
                client = tweepy.Client(credential.bearer_token, credential.consumer_key,
                                    credential.consumer_secret, credential.access_key, credential.access_secret, wait_on_rate_limit=True)
                client.get_tweet('474141231996350466') 
                credentials_validity[credential.name] = 200
            except Unauthorized:
                credentials_validity[credential.name] = 401
            except Forbidden:
                credentials_validity[credential.name] = 403
            except TooManyRequests:
                credentials_validity[credential.name] = 429
        
        return credentials_validity

    def check_crypto_address(self, tweet):
        reply = None
        if (any(word in tweet for word in ["drop", "comment", "put", "reply"])) and (any(w in tweet for w in ["address", "wallet", "$eth", "$sol","eth","sol"])):
            if(any(w in tweet for w in ["sol", "solana"])):
                reply = random.choice([" SOL address : {}".format(self.eth_addr)," sol : {}".format(self.eth_addr), self.sol_addr ])
            else:
                reply = random.choice([" ETH address : {}".format(self.eth_addr)," eth : {}".format(self.eth_addr), self.eth_addr ])
        return reply


            

        







        
    
