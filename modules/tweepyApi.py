import tweepy

def getTweepyApi():
    CONSUMER_KEY = '969pjywgoM9mr40Q7dpfhA5zm'
    CONSUMER_SECRET = 'L9FRWifMS8lJ72ojj9y9dtYj7pDDWpzmg3wngDh71nIKNP72Rb'
    ACCESS_TOKEN = '1558983421778890752-cLwTeeSk4IpNhbsIRWKW3SdQy0MA2T'
    ACCESS_SECRET = 'LUejAC2W4k15EB58YF6qf4pGOJZ5wJ3cV4Q8RxeBMvExP'

    # twitter認証
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    return api
