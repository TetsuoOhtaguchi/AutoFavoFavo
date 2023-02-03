import random
import time
import math

from modules import tweepyApi

"""
指定したアカウントをフォローしているアカウントに対して、いいねを行う

ポイント：アピールしたいアカウントに認知してもらうことができるようになる
"""
api = tweepyApi.getTweepyApi()

# 処理回数の上限を定義する
limitNum = 3

# 処理カウンター
counter = 0

# シャッフルしたフォロワーを最初からn人目までをピックアップするか定義する
targetNum = 15

# 待機時間を定義する
sleepTime = 60 * 15

for i in range(0, 100, 1):
    # 処理カウンターを加算する
    counter += 1

    # @から後のユーザーネームを入れる
    # @topitmedia @freedomissla @ito_marketer
    screenName = "ito_marketer"

    followers_id_list = api.get_follower_ids(screen_name=screenName)
    random.shuffle(followers_id_list)

    # ピックアップしたフォロワーに対してイイねを行う
    for follower_id in followers_id_list[:targetNum]:
        tweets = api.user_timeline(id=follower_id, count=1,  page=follower_id)
        for tweet in tweets:
            if (not tweet.retweeted) and (not tweet.favorited) and ('RT @' not in tweet.text):
                # イイねを行う
                api.create_favorite(tweet.id)
                print(tweet.id, 'イイねを行う')
                time.sleep(5)

    if counter == limitNum:
         # 処理カウンターが上限に達した場合、処理を終了する
        print('処理が終了しました')
        break
    else:
        # n秒間待機する
        sleepMinute = math.floor(sleepTime / 60)
        print("処理{0}回目です。{1}分間待機します".format(counter, sleepMinute))
        time.sleep(sleepTime)