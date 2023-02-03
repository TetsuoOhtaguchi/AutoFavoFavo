import tweepy
import pandas as pd

from datetime import timedelta
from modules import tweepyApi

"""
対象アカウントのツイートをまとめて取得する
"""
api = tweepyApi.getTweepyApi()

tweet_timeline = api.user_timeline()

# @から後のユーザーネームを入れる
screenName = "freedomissla"

tweet_data = []
num = 0
for page in range(17):
    tweets = api.user_timeline(screen_name=screenName, count=10, page=page)

    for tweet in tweets:
        tweet.created_at += timedelta(hours=9)
        num += 1
        tweet_data.append(['@'+screenName, tweet.created_at, tweet.text])

print(num, '件のツイート表示しました')

# ツイートデータをデータフレームに変換
tweet_data = pd.DataFrame(tweet_data, columns=["account", "date", "tweet"])
# ファイル出力
fileName = input("ファイル名を入力してください：")
tweet_data.to_csv(fileName + ".csv")
print("「" + fileName + ".csv」が作成されました。")