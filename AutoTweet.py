from modules import tweepyApi

"""
自動ツイートを行う
"""
api = tweepyApi.getTweepyApi()

# 内容 改行なしの場合
noNewLineContents = "test tweet2 from python"
# print('【改行なしの場合】', noNewLineContents)

# 内容 改行ありの場合
# newLineContents = [
#     'test tweet 1',
#     'test tweet 2',
#     'test tweet 3',
#     'from python'
# ]
# newLineContent = '\n'.join(newLineContents)
# print('【改行ありの場合】', newLineContent)

api.update_status(noNewLineContents)