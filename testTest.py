from modules import GetTargetUserPopularTweets
import random

# 人気ツイートリスト
popularTweetsList = GetTargetUserPopularTweets.getTargetUserPopularTweetsArr(screenName='freedomissla')

# ランダムに1ツイート取得する
random.shuffle(popularTweetsList)
print(popularTweetsList[0])