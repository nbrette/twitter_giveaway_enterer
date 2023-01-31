from firebase_admin import credentials
from firebase_admin import firestore
from controllers.firestore_controller import FirestoreController
from controllers.twitter_controller import TwitterController

fs_controller = FirestoreController()
available_credentials = fs_controller.get_config('jacky')
twitter_controller = TwitterController(available_credentials)
twitter_controller.get_recent_tweets('giveaway')
# config = fs_controller.get_config('jacky')
# twitter_controller = TwitterController(config)
# twitter_controller.verify_credentials([config.credentials])

