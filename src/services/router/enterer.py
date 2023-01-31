import logging
from fastapi import APIRouter, HTTPException
from models.enter_request import EnterRequest 
from controllers.firestore_controller import FirestoreController
from controllers.twitter_controller import TwitterController

router = APIRouter()

@router.post("/enter/recents")
async def enter_recents_giveaway(request : EnterRequest):
    giveaway_entered = 0
    fs_controller = FirestoreController()
    config = fs_controller.get_config(request.account)
    print(config)

    logging.debug(config)
    twitter_controller = TwitterController(config)
    try:
        tweets = twitter_controller.get_recent_tweets(research='giveaway')
    except Exception as err:
        raise HTTPException(status_code=500, detail="Error when getting the latest tweets")

    for tweet in tweets:
        if (twitter_controller.check_is_contest(tweet.text) and twitter_controller.check_contains_bannedwords(tweet.text) is False):
            try:
                twitter_controller.enter_giveaway(tweet)  
                giveaway_entered+=1
                logging.debug(f'Giveaway entered tweet : {tweet.id}')
            except Exception as err:
                logging.error(f'Error when entering tweet {tweet.id} : {err}')
    
    return {'giveaway_entered' : giveaway_entered}

@router.get('/check_credentials')
async def check_available_credentials():
    fs_controller = FirestoreController()
    available_credentials = fs_controller.get_every_credentials()
    twitter_controller = TwitterController()
    return twitter_controller.verify_credentials(available_credentials)    





