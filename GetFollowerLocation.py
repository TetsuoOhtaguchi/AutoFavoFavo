import tweepy
import time

import pandas as pd
from modules import tweepyApi
"""
特定のアカウントをフォローしているアカウントのロケーションを取得する
"""
api = tweepyApi.getTweepyApi()

# 特定の@ユーザーネーム
screenName = "freedomissla"

# フォロー人数カウンター
counter = 0

# フォローの上限人数
limit = 30

# 対象ユーザーのフォロワーリスト
followers_id_list = api.get_follower_ids(screen_name=screenName)

# ユーザー情報リスト
user_data_list = []
num = 0
# フォロワーIDに対し、フォロー処理を行う
for follower_id in followers_id_list:
    user = api.get_user(user_id=follower_id)
    targetLocation = user.location
    if '石川' in targetLocation or '金沢' in targetLocation or '富山' in targetLocation or '福井' in targetLocation:
        num += 1
        user_data_list.append(['@{}'.format(user.screen_name), 'ロケーション：{}'.format(targetLocation)])
        print('{0}件目 @{1} ロケーション：{2}'.format(num, user.screen_name, targetLocation))

if num == 0:
    print('検出されたユーザー情報は0件です')
else:
    print('{}件のユーザー情報を取得しました'.format(num))
    saveState = input("保存しますか？y/n:")
    if saveState == 'n':
        print('処理を終了しました。')
    elif saveState == 'y':
        # ユーザー情報をデータフレームに変換
        user_data_list = pd.DataFrame(user_data_list, columns=["user", "location"])
        # ファイル出力
        fileName = input("ファイル名を入力してください:")
        user_data_list.to_csv("UserList@" + fileName + ".csv")
        print("「" + fileName + ".csv」が作成されました。")
    else:
        print('入力情報が誤っています:{}'.format(saveState))