import pandas as pd
import datetime

from datetime import timedelta
from modules import tweepyApi

"""
対象アカウントのツイートをまとめて取得する
"""
api = tweepyApi.getTweepyApi()

tweet_timeline = api.user_timeline()

# 現在の日時
time_now = datetime.datetime.now()

# @から後の特定のユーザーネームを入れる
screenName = "nagoken_s"

# 指定開始日
startDay = 30

# 指定終了日
endDay = 60

# イイねの条件件数
favoriteCount = 100

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
            tweetDateYMD = "{0:%Y/%m/%d}".format(tweet.created_at)
            tweet_data.append([tweetDateYMD, 'イイね数{}件'.format(tweet.favorite_count), '＜内容＞:{}'.format(tweet.text)])

if num == 0:
    print('検出されたツイートは0件です')
else:
    print('{}件のツイート表示しました'.format(num))
    # ツイートデータをデータフレームに変換
    tweet_data = pd.DataFrame(tweet_data, columns=["date", "favo", "tweet"])
    # ファイル出力
    fileName = input("ファイル名を入力してください：")
    tweet_data.to_csv(fileName + ".csv")
    print("「" + fileName + ".csv」が作成されました。")