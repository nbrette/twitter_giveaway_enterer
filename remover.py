import tweepy
import utils
import argparse

parser = argparse.ArgumentParser(description='Optional app description')
# Optional argument
parser.add_argument('--sort', type=str,
                    help='Asc or desc to begin with newer or oldwer followers')

# Switch
parser.add_argument('--nb', type=int,
                    help='Number of account you want to unfollow')
args = parser.parse_args()
print(args.nb)
print(args.sort)
config = utils.load_configfile("config.json")
client = tweepy.Client(config[utils.BEARER_TOKEN], config[utils.CONSUMER_KEY],
                            config[utils.CONSUMER_SECRET], config[utils.ACCESS_KEY], config[utils.ACCESS_SECRET])
user = client.get_user(username="gimmethepackage")
print(user.data["id"])
id = user.data["id"]
followed = client.get_users_following(id, max_results=1000)

ids = []
for f in followed.data:
    ids.append(f.id)

if (args.sort == "desc"):   
    ids.reverse()
print(type(ids[1]))
client.unfollow_list(list_id="145844")

