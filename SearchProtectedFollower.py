import tweepy
import pandas as pd

from modules import tweepyApi
"""
特定のアカウントをフォローしている鍵垢のアカウントを探す
"""
api = tweepyApi.getTweepyApi()

# 特定の@ユーザーネーム
screenName = "freedomissla"

# 対象ユーザーのフォロワーリスト
followers_id_list = api.get_follower_ids(screen_name=screenName)

# ユーザーリスト
user_list = []
num = 0
# フォロワーIDに対し、フォロー処理を行う
for follower_id in followers_id_list:
    user = api.get_user(user_id=follower_id)

    try:
        if user.following == False and user.protected == True and user.follow_request_sent == False and user.friends_count < 100 and user.followers_count < 100:
         # フォローしていない/フォローリクエスト未送信/フォロー数が100以下/フォロワー数が100以下/の鍵垢の場合、以下の処理を行う
            num += 1
            user_list.append(['@{}'.format(user.screen_name), 'フォロー:{}'.format(user.friends_count), 'フォロワー:{}'.format(user.followers_count)])
            print('{0}件目, @{1}, フォロー:{2}, フォロワー:{3}'.format(num, user.screen_name, user.friends_count, user.followers_count))
    except tweepy.TweepError as e:
            print(e)

if num == 0:
    print('検出されたユーザー情報は0件です')
else:
    print('{}件のユーザー情報を取得しました'.format(num))
    saveState = input("保存しますか？y/n:")
    if saveState == 'n':
        print('処理を終了しました。')
    elif saveState == 'y':
        # ユーザー情報をデータフレームに変換
        user_list = pd.DataFrame(user_list, columns=["user", "friends", "followers"])
        # ファイル出力
        fileName = input("ファイル名を入力してください:")
        user_list.to_csv("UserList@" + fileName + ".csv")
        print("「" + fileName + ".csv」が作成されました。")
    else:
        print('入力情報が誤っています:{}'.format(saveState))