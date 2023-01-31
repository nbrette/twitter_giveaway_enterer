import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import tweepy
from controllers.firestore_controller import FirestoreController
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# with open('tweet.txt') as file:
#     lines = [line.rstrip() for line in file]
#     print(lines)

# config = db.collection(u'admin').document(u'config').set ({'sentences' : lines}, merge=True)

# controller = FirestoreController()
# config = controller.get_credentials('jacky')
# client = tweepy.Client(config.bearer_token, config.consumer_key,
#                                     config.consumer_secret, config.access_key, config.access_secret, wait_on_rate_limit=True)
# response = client.search_recent_tweets(
#             query='twitch', max_results=100, tweet_fields=["entities", "created_at"], user_fields=['profile_image_url', 'username'], expansions=['author_id'])
# tweets = response.data

# usernames = []
# # You can then access those objects in the includes Response field
# includes = response.includes
# users = includes["users"]
# for user    in users:
#     usernames.append(user.username)
# with open('users.txt', 'a') as f:
#     f.writelines('%s\n' % word for word in usernames)
import datetime

now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))

