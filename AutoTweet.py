from modules import tweepyApi

import csv

"""
自動ツイートを行う
"""
api = tweepyApi.getTweepyApi()

# 内容 改行なしの場合
tweet_text = "test tweet3 from python"
# print('【改行なしの場合】', noNewLineContents)

# 自分の全ツイートを入れる配列
my_all_tweets = []

# 直近の200ツイート分を取得しておく
latest_tweets = api.user_timeline(count = 200)
my_all_tweets.extend(latest_tweets)

# 取得するツイートが無くなるまで続ける
while len(latest_tweets) > 0:
    latest_tweets = api.user_timeline(count = 200, max_id = my_all_tweets[-1].id - 1)
    my_all_tweets.extend(latest_tweets)

# 投稿済みのツイートか確認する
def checkTweet():
    for tweet in my_all_tweets:
        if (tweet.text.startswith('RT')) or (tweet.text.startswith('@')):
            # RTとリプライはスキップ
            continue
        else:
            if tweet.text == tweet_text:
                # 投稿済み
                return tweet_text
            else:
                #
                return '投稿可能です'

tweetCheckResult = checkTweet()

if tweetCheckResult != '投稿可能です':
    # 既に内容が投稿済みの場合、処理を終了する
    print('※こちらの内容はすでにツイート済みです※')
else:
    # 投稿可能な場合
    print('【{0}】{1}'.format(tweetCheckResult, tweet_text))
    # 投稿確認を行う
    go_tweet = input("ツイートする場合Goと入力してください：")
    if go_tweet != 'Go':
        # 'Go'を入力しなかった場合、ツイートキャンセルする
        print('ツイートをキャンセルしました')
    else:
        # ツイートを行う
        print('【Go Tweet🚀】{}'.format(tweet_text))
        api.update_status(tweet_text)
