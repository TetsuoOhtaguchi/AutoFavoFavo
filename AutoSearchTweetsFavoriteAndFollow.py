import tweepy
import time

from modules import tweepyApi

"""
検索キーワードから自動フォロー、自動いいねを行う
"""
api = tweepyApi.getTweepyApi()

# 検索キーワード
query = 'プログラミング'
count = 5

# 検索実行
results = api.search_tweets(q=query, count=count)

for result in results:
    user_key = result.id
    screen_name = result.user.screen_name
    print('@' + screen_name + 'をフォロー処理中...')
    for i in range(3): #RateLimitにかかったら3回までリトライ
        try:
            if result.lang == 'ja':
                api.create_favorite(user_key)
                api.create_friendship(screen_name=screen_name)
                print('@' + screen_name + 'さんのフォローに成功しました。')
            else:
                print('@' + screen_name + 'さんは日本語アカウントではありません。')
        except tweepy.TweepError as e:
            if e.reason == "[{'message': 'Rate limit exceeded', 'code': 88}]":
               print(e)
               time.sleep(15 * 60) #15分待機
            else:
               break
        else:
            time.sleep(5)
            break