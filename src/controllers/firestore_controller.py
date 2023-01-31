import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from models.twitter_account_credentials import TwitterAccountCredentials
from models.config import Config
from typing import Dict, List


class FirestoreController():

    ADMIN_COLLECTION = u'admin'
    LOG_COLLECTION=u'logs'
    ENTRY_LOG_DOCUMENT = u'giveaway_entry'
    CONFIG_DOCUMENT = u'config'
    CREDENTIALS_DOCUMENT = u'credentials'
    BANNED_WORDS = u'banned_words'
    ETHEREUM_ADDRESS = u'eth_address'
    SOLANA_ADDRESS = u'sol_address'
    SENTENCES = u'sentences'
    USERNAMES = u'usernames'


    def __init__(self) -> None:
        cred = credentials.ApplicationDefault()
        if not firebase_admin._apps:
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()
    
    def get_credentials(self, account_name) -> TwitterAccountCredentials :
        """
        Get the credentials document and then get the credentials for the account given in parameter
        """
        
        credentials_doc = self.db.collection(self.ADMIN_COLLECTION).document(self.CREDENTIALS_DOCUMENT).get()

        try:
            credentials = credentials_doc.to_dict()[account_name]
        except KeyError as err:
            raise Exception(f'Could not find credentials for the account {account_name}') from err

        return TwitterAccountCredentials(credentials['bearer_token'], credentials['access_key'], credentials['access_secret'], credentials['consumer_key'], credentials['consumer_secret'])

    def get_config(self, account_name) -> Config:
        config_document = self.db.collection(self.ADMIN_COLLECTION).document(self.CONFIG_DOCUMENT).get().to_dict()
        credentials = self.get_credentials(account_name)
        config = Config(credentials, config_document[self.BANNED_WORDS], config_document[self.ETHEREUM_ADDRESS], config_document[self.SOLANA_ADDRESS], config_document[self.SENTENCES], config_document[self.USERNAMES])
        return config
    
    def get_every_credentials(self) -> List[TwitterAccountCredentials]:
        available_credentials = []
        credentials_doc = self.db.collection(self.ADMIN_COLLECTION).document(self.CREDENTIALS_DOCUMENT).get()
        for key, cred in credentials_doc.to_dict().items():
            available_credential = TwitterAccountCredentials(cred['bearer_token'], cred['access_key'], cred['access_secret'], cred['consumer_key'], cred['consumer_secret'], key)
            available_credentials.append(available_credential)
        return available_credentials





    



    