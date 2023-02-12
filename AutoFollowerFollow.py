import tweepy
import time

from modules import tweepyApi
"""
特定のアカウントをフォローしているアカウントに対して、フォローを行う
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

# フォロワーIDに対し、フォロー処理を行う
for follower_id in followers_id_list:
    # フォロー数が10名または20名に達した場合
    if counter == 10 or counter == 20:
        print('フォロー数が{}名に達したため、20分間待機します。'.format(counter))
        time.sleep(60 * 20)

    # フォロー数が30名に達した場合
    if counter == limit:
        # 上限に達した場合、処理を終了する
        print("----- 処理終了 -----")
        break

    #RateLimitにかかったら2回までリトライする
    for i in range(2):
        # ユーザー情報
        user = api.get_user(user_id=follower_id)
        print('処理中...')
        try:
            if user.following == False and user.screen_name != 'ohtaguchi_t' and user.protected == True and user.follow_request_sent == False:
                # フォローしていない鍵垢の場合、以下の処理を行う
                counter += 1
                # todo api.create_friendship(user_id=follower_id)
                print('{0}人目：@{1}さんをフォローしました'.format(counter, user.screen_name))

            else:
                print('@{}さんはフォロー対象外です'.format(user.screen_name))

        except tweepy.TweepError as e:
            if e.reason == "[{'message': 'Rate limit exceeded', 'code': 88}]":
                print(e)
                time.sleep(15 * 60) #15分待機
            else:
                break

        else:
            time.sleep(5)
            break