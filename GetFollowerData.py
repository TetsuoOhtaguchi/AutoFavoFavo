import tweepy
import pandas as pd

from modules import tweepyApi

"""
対象のアカウントから、以下のフォロワー情報を取得する

Name: 名前
Following: フォローしているか否か（フォローしている場合true）
Follow_Request_Sent: フォローリクエストを送信しているか否か（送信している場合true）
Protected: ツイートを非公開にしているか（非公開の場合true）
"""
api = tweepyApi.getTweepyApi()

# @から後のユーザーネームを入れる
screenName = "freedomissla"

followerIDs = tweepy.Cursor(api.get_follower_ids, screen_name=screenName, cursor=-1).items()

followerDatas = []
for followerID in followerIDs:
    followerData = {}
    data = api.get_user(user_id=followerID)
    followerData["Name"] = data.name
    followerData["Following"] = data.following
    followerData["Follow_Request_Sent"] = data.follow_request_sent
    followerData["Protected"] = data.protected
    followerDatas.append(followerData)

#表示最大行数
pd.set_option("display.max_rows", 1000)
df = pd.DataFrame(followerDatas).loc[:,["Name","Following","Follow_Request_Sent","Protected"]]

# ファイル出力
fileName = input("ファイル名を入力してください：")
df.to_csv(fileName + ".csv")
print("「" + fileName + ".csv」が作成されました。")