import tweepy
import datetime

from datetime import timedelta

CONSUMER_KEY = '969pjywgoM9mr40Q7dpfhA5zm'
CONSUMER_SECRET = 'L9FRWifMS8lJ72ojj9y9dtYj7pDDWpzmg3wngDh71nIKNP72Rb'
ACCESS_TOKEN = '1558983421778890752-cLwTeeSk4IpNhbsIRWKW3SdQy0MA2T'
ACCESS_SECRET = 'LUejAC2W4k15EB58YF6qf4pGOJZ5wJ3cV4Q8RxeBMvExP'

# twitter認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

"""
対象アカウントの人気ツイートをまとめて取得する
"""
def getTargetUserPopularTweetsArr(screenName, startDay = 30, endDay = 60, favoriteCount = 100):
    # 現在の日時
    time_now = datetime.datetime.now()

    # ツイートを格納する配列
    tweet_data = []
    num = 0
    for page in range(17):
        tweets = api.user_timeline(screen_name=screenName, count=10, page=page)

        for tweet in tweets:
            tweet.created_at += timedelta(hours=9)
            # 現在時刻からツイート時刻を差し引いた時差
            timeDifference = time_now - tweet.created_at.replace(tzinfo=None)
            # 現在の日時より30日以上60日以下の日付で投稿されたツイートのみ取得する
            if timeDifference > datetime.timedelta(days=startDay) and timeDifference <= datetime.timedelta(days=endDay) and tweet.favorite_count >= favoriteCount:
                num += 1
                tweet_data.append(tweet.text)

    if num == 0:
        print('検出されたツイートは0件です')
        return ['検出されたツイートは0件です']
    else:
        print('{}件のツイート取得しました'.format(num))
        return tweet_data